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

debug = False

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    
    print("fname: " + fname)
    with open(fname, 'rb') as infile:
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close

        return text


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
    i = -1
    k = 0
    j = 0
    appendString = []
    for text in binaryFile:
        lineNumber = lineNumber + 1
        text = text.rstrip()


        if lineNumber <= 15:
            if lineNumber == 8:
                jsonDict["Meeting"]["committee"] = str(text).rstrip()
                print("Committee: " + str(text).rstrip())
            elif lineNumber == 10:
                jsonDict["Meeting"]["title"] = text.rstrip()
                print("Title: " + str(text).rstrip())
            elif lineNumber == 12:
                jsonDict["Meeting"]["date"] = text.rstrip()
                print("Date: " + str(text).rstrip())
            elif lineNumber == 13:
                jsonDict["Meeting"]["location"] = text.rstrip()
                print("Location: " + str(text).rstrip())
            elif lineNumber == 14:
                jsonDict["Meeting"]["time"] = text.rstrip()
                print("Time: " + str(text).rstrip())

        else:

            if i > len(splitStrings)-2:
                return jsonDict

            if splitStrings[i+1] in str(text):
                startedBool = True
                i = i + 1
                print("TRIGGER WARNING i=" + str(i))


                if i > 0:

                    #Build format into aditional
                    jsonDict["Meeting"]["subsection"].append({"sub_Title": None, "Items": [{"index_in_pdf": None,
                          "separate_index":None, "item_title":None, "pages_start":None, "pages_end":None, "text":None,
                          "presenters": [ { "name":None } ], "keywords": [ None, None ], "discussion":None, "purpose":None }]})

                    print("Appending Items for " + str(splitStrings[i]))
                    jsonDict["Meeting"]["subsection"][i]["Items"] = appendString
                    appendString = []

                else:
                    jsonDict["Meeting"]["subsection"][i]["Title"] = splitStrings[i]
            else:
                if startedBool:

                    if str(text) == "\n":
                        pass
                    elif str(text) == " \n":

                        pass
                    else:
                        appendString.append(str(text).rstrip())
                        print("|| " + splitStrings[i + 1] + ":::" + str(text))

                # String comparisons unique to "Opening Minuets"
                if i == 0:
                    # Append all Attendees not on StopWord List
                    if text.rstrip() not in nonAttendance:
                        jsonDict["Meeting"]["attendees"].append(str(text))
                        #print("Appended Attendee: " + str(text))
                    else:
                        #print("Rejected; " + text)
                        pass

                # String comparisons unique to "Discussion Minuets"
                if i == 1:
                    pattern = re.compile("\d\.")
                    if pattern.match(text) != None:
                        print("ITEM NUMBER: " + text.strip("."))
                        jsonDict["Meeting"]["subsection"][1]["Items"].append({"index_in_pdf": None,
                                                                                "separate_index": None,
                                                                                "item_title": None,
                                                                                "pages_start": None,
                                                                                "pages_end": None,
                                                                                "text": None,
                                                                                "presenters": [
                                                                                {"name": None}],
                                                                                "keywords": [None, None],
                                                                                "discussion": None,

                        #itemNumber = int(text.strip("."))










    #filePointers = []
    #fileName = fileName.split(".",1)
    #fileName = fileName[0]
    #output = convert(fileName + ".pdf")
    print()

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

