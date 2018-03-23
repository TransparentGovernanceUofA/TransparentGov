'''
    import pdfquery
    pdf = pdfquery.PDFQuery("pdfs/Combined-agenda-and-documents.pdf")
    pdf.load()
    pdf.tree.write('test.xml', pretty_print=True)
    '''
# Adapted from https://reachtim.com/articles/PDF-Manipulation.html
# Updated to python 3 by Austin Crapo
# File Split Implemented by Gregory Gould
from io import StringIO
import sys, re
import os
import json
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from data import *
from tika import parser

debug = False

def convert(fname, pages=None):
    parsedPDF = parser.from_file(fname)
    return parsedPDF["content"]


def parse(fileName, filePointers):
    print(filePointers)
    lineCount = 0
    pageCount = 0
    i= 0
    file = open(fileName,'rb')
    date = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for text in file:
        # Line Count to show progress
        lineCount = lineCount + 1
        if lineCount < 10:
            for day in date:
                if day in str(text):
                    newName = str(text)
                    print("Date: " + newName)
                    print("Renaming")
                    newName = newName.split(", ",1)
                    print(newName)
                    newName = newName[1]
                    newName = newName[:-4]

                    pdfName = fileName.split(".",1)
                    pdfName = pdfName[0]
                    print("pdfName: " + pdfName)

                    print("newName: " + path + newName)
                    #os.rename(pdfName + ".pdf", path + "/Approved_Minutes " + newName + ".pdf")
                    #os.rename(pdfName + ".txt", path + "/Approved_Minutes " + newName + ".txt")

            if (lineCount % 23 == 0): #23 lines/page at 12pt font
                pageCount = pageCount + 1
                print("Pages Printed: "+str(pageCount))
            # Read lines
            if keywords[i] in text:
                i = i + 1
            #print("i: "+str(i-1)+"|"+str(keywords[i-1]))
            if i > 0:
                #print("Prewrite i: " + str(i-1))
                #print(filePointers)
                filePointers[i-1].write(text)






def processMinFile(filePath, jsonDict, fileName):
    #if not os.path.exists(path + "/" + fileName):
    #    os.makedirs(path + "/" + fileName)
    print(filePath)
    binaryFile = open(filePath, 'r')
    #textFile = binaryFile.read().decode("utf-8")

    itemNumber = 0

    lineNumber = 0
    splitNames = ["ATTENDEES", "OPENING_SESSION", "DISCUSSION_ITEMS", "ACTION_ITEMS", "QUESTION_PERIOD",
                  "INFORMATION_REPORTS", "CLOSING_SESSION"]
    splitStrings = ["ATTENDEES", "OPENING SESSION", "DISCUSSION ITEMS", "ACTION ITEMS", "DISCUSSION ITEMS",
                    "INFORMATION REPORTS", "CLOSING SESSION"]

    startedBool = False
    subsectionNumber = -1
    k = 0
    j = 0
    itemNumber = 0
    textAcc = []
    isCarried = False


    pageNumber = 0
    appendString = []
    for text in binaryFile:
        lineNumber = lineNumber + 1
        text = text.rstrip()

        '''
        if text == "":
            continue
        '''
        # Append basic meeting information found in same place.
        if lineNumber <= 65:
            if lineNumber == 56:
                jsonDict["Meeting"]["committee"] = str(text).rstrip()
                print("Committee: " + str(text).rstrip())
            elif lineNumber == 57:
                jsonDict["Meeting"]["title"] = text.rstrip()
                print("Title: " + str(text).rstrip())
            elif lineNumber == 60:
                jsonDict["Meeting"]["date"] = text.rstrip()
                print("Date: " + str(text).rstrip())
            elif lineNumber == 61:
                jsonDict["Meeting"]["location"] = text.rstrip()
                print("Location: " + str(text).rstrip())
            elif lineNumber == 62:
                jsonDict["Meeting"]["time"] = text.rstrip()
                print("Time: " + str(text).rstrip())

        else: # Do these comparisons when lineNumber >= 65

            # Return if no more preprogrammed sections
            if subsectionNumber > len(splitStrings)-2:
                return jsonDict

            # Check if the prepgrammed section is in the text
            if splitStrings[subsectionNumber+1] in str(text):
                startedBool = True
                subsectionNumber = subsectionNumber + 1
                print("SUBSECTION NUMBER: " + str(subsectionNumber))

                if subsectionNumber > 0:

                    #Build additional subsections
                    print("## ADDING Subsection!")
                    jsonDict["Meeting"]["subsection"].append({"sub_Title": None, "Items": [{"index_in_pdf": None,
                          "separate_index":None, "item_title":None, "pages_start":None, "pages_end":None, "text":None,
                          "presenters": [ { "name":None } ], "motions": [{ "motion":None, "carried":None, "content":None }],
                          "keywords": [ None, None ], "discussion":None, "purpose":None }]})

                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Title"] = splitStrings[subsectionNumber]

                    #print("Appending Items for " + str(splitStrings[subsectionNumber]))
                    #jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["text"] = appendString
                    #appendString = []

                else: # On the first time, just append title.
                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Title"] = splitStrings[subsectionNumber]
            else:
                if startedBool:

                    if str(text) == "\n":
                        pass
                    elif str(text) == " \n":
                        pass

                    else:
                        appendString.append(str(text).rstrip())
                        if (subsectionNumber > 0):
                            print(str(lineNumber) + " || " + splitStrings[subsectionNumber + 1] + ":::" + str(text))

                if "Page" in text:
                    pageText = text.split("Page ")
                    print("New Page! Page: " + str(pageText[1]))
                    pageNumber = int(pageText[1])


                pattern = re.compile("\d\.")
                pattern2 = re.compile("\d\d\.")

                # Pattern for matching item numbers "Number + dot (.)"
                if pattern.match(text) != None or pattern2.match(text) != None:
                    itemNumber += 1  # Matching matches
                    number = text.split(".")
                    number = number[0]

                    if itemNumber > 1:  # Append discussion text
                        print("Subsection Number: " + str(subsectionNumber) + " Item Number: " + str(itemNumber))
                        jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber - 1]["discussion"] = textAcc
                        print("Discussion Text Appended")

                    textAcc = []  # Reset Discussion Text

                    print("ITEM NUMBER: " + number + " itemNumber: " + str(itemNumber))

                    # Append Additional Item to JSON format.
                    print("ADDING ITEM :: Subsection Number: " + str(subsectionNumber) + " Item Number: " + str(itemNumber))
                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"].append({"index_in_pdf": None,
                                                                          "separate_index": None, "item_title": None,
                                                                          "pages_start": None,
                                                                          "pages_end": None, "text": None,
                                                                          "presenters": [{"name": None}], "motions": [
                                                                          {"motion": None, "carried": None, "content": None}],
                                                                          "keywords": [None, None], "discussion": None,
                                                                          "purpose": None})

                    # Append Page Number

                    #print("# Subs: " + str(len(jsonDict["Meeting"]["subsection"])))
                    #print("# Items: " + str(len(jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"])))
                    #print(type(jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"]))
                    #print(jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"])

                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["index_in_pdf"] = str(
                        number)
                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["pages_start"] = str(pageNumber)

                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber-1]["pages_end"] = str(pageNumber)


                # String comparisons unique to "Opening Minuets"
                if subsectionNumber == 0:
                    # Append all Attendees not on StopWord List
                    if text.rstrip() not in nonAttendance:
                        jsonDict["Meeting"]["attendees"].append(str(text))
                        #print("Appended Attendee: " + str(text))
                    else:
                        #print("Rejected; " + text)
                        pass

                # String comparisons unique to "Discussion Minuets"
                if subsectionNumber == 1:

                    if "Motion:" in text:
                        print("Motion Detected!")
                        newText = text.split(':')
                        newText = newText[1]
                        print("Motion Title: " + newText)
                        jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["motions"][0]["motion"] = str(newText)
                        isCarried = True

                    if "THAT" in text:
                        jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["motions"][0]["content"] = text
                        print("Motion Content: " + text)

                    if isCarried == True:
                        if "CARRIED" in text:
                            jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["motions"][0]["carried"] = True
                            isCarried = False
                            print("Motion Carried: " + "True")

                    textAcc.append(text)
                    #print("Continue..")

                if subsectionNumber >= 2:


                    if "Presenter(s)" in text:
                        newText = text.strip("Presenter(s): ")

                        jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["presenters"] = newText
                        print("Presenter detected and assigned: " + newText)

                    if "Purpose of the Proposal:" in text:
                        newText = text.strip("Purpose of the Proposal: ")
                        jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["Purpose"] = newText
                        print("Presenter detected and assigned: " + newText)

                    textAcc.append(text)




                        #itemNumber = int(text.strip("."))










    #filePointers = []
    #fileName = fileName.split(".",1)
    #fileName = fileName[0]
    #output = convert(fileName + ".pdf")


    '''
    # Create Files for each individual piece of text
    i = 0
    while (i < numberSplit):
        if not os.path.exists(path + "/" + fileName):
            os.makedirs(path + "/" + fileName)
            keywords.append(splitStrings[i].encode('utf-8'))
            fp = open(path + "/" + fileName + "/" + fileName + "_" + splitNames[i], 'wb')
            filePointers.append(fp)
            #print(str(splitNames[i])+" Pointer i: "+str(i))
            i = i + 1
    
    
    keywords.append(splitStrings[0].encode('utf-8')) #Add an extra
    
    parse(path + "/" + fileName + ".txt", filePointers)
    
    # Close files
    for file in filePointers:
        #print("Closing: " + str(file))
        file.close()
        print()	
        print(fileName + " is finished being processed")
    '''



def isPDF(file):
    file1 = file.split(".",1)
    file1 = file1[1]
    
    if file1 == "pdf":
        print(file + " - is PDF")
        return True
    else:
        
        return False


#####################################	
########## main program #############
#####################################

print("PDF Scraper Started \n\n")



data = json.loads(jsonDict)

filePath = "2013" #Path to File

### Dissecting the Approved Minutes ###

# For each file in the
for file in os.listdir(filePath):
    current = os.path.join(filePath, file)
    print("Current: " + current)
    if os.path.isfile(current):
        if isPDF(file):

            print("Begin Process of Scraping: " + file)
            fileName = file.split(".",1)
            fileName = fileName[0] #Get a filename without .pdf

            print("FILE NAME: " + fileName)
            fh = open(filePath + "/" + fileName + ".txt", "w")
            output = convert(current)
            #output = output.decode('cp1250').encode('utf-8')

            with open(filePath + "/" + 'JASON.txt', 'w') as outfile:
                json.dump(data, outfile)

            fh.write(output)
            fh.close()  # Save text stripped PDF

            print("Saved text stripped PDF as: " + filePath + "/" + fileName + ".txt")
            data = processMinFile(filePath + "/" + fileName + ".txt", data, fileName)

            with open('JASON.txt', 'w') as outfile:
                json.dump(data, outfile)

        else:
            print(file + ": failed, not pdf")

