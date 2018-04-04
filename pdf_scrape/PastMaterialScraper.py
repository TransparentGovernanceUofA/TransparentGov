'''
 Name:         Gregory Gould
 ONE Card #:   1406575
 Unix ID:      gsgould
 CLASS:        CMPUT401
'''

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

debug = True

#####################################
########## convert      #############
# Converts PDF 2 Text using Apache  #
# TIKA                              #
#####################################
def convert(fname, pages=None):
    parsedPDF = parser.from_file(fname)
    return parsedPDF["content"]

#####################################
########## convertJSON  #############
# Glorified string matching func    #
#                                   #
#####################################

def appendJSON(filePath, jsonDict):

    print(filePath)
    binaryFile = open(filePath, 'r')
    lineNumber = 0
    endName = "CLOSING SESSION"
    startedBool = False
    k = 0
    j = 0
    itemNumber = 0
    appendText = []
    itemChanged  = False
    previousItem = ""
    backup = ""

    for text in binaryFile:
        lineNumber = lineNumber + 1
        text = text.rstrip()

        '''
        if text == "":
            continue
        '''
        # Append basic meeting information found in same place everytime.
        ## TODO: Make dynamic.


        if lineNumber <= 68:

            if lineNumber == 63:
                if jsonDict["Meeting"]["date"] == text.rstrip():
                    if debug: print("GOOD")
                else:
                    print("Your Summary File and Documents File don't match!")
                    exit(1)


        else: # Do these comparisons when lineNumber >= 65
                if debug: print(str(lineNumber) + " || " +  "::: " + str(text))

                if not startedBool:
                    pattern = re.compile("\d\.")
                    pattern2 = re.compile("\d\d\.")

                    # Pattern for matching item numbers "Number + dot (.)"
                    if pattern.match(text) != None or pattern2.match(text) != None:
                        itemNumber += 1  # Matching matches
                        if debug: print("itemNumber: " + str(itemNumber))

                    if endName in text:
                        if debug: print("End of Table of Contents")
                        startedBool = True

                else:
                    pattern2 = re.compile("Item \d")
                    pattern = re.compile("Item No. \d")
                    if pattern.match(text) != None or pattern2.match(text) != None:

                        if pattern.match(text) != None:
                            processText = text.strip("Item No. ")
                            processText = re.sub("\D", "", processText)

                        elif pattern2.match(text) != None:
                            processText = text.strip("Item ")
                            processText = re.sub("\D", "", processText)


                        if previousItem == processText:
                            if debug: print("Don't Change")

                        else:
                            if debug: print("Item Discovered!")
                            #if debug: print("Previous Item: " + previousItem + " Backup: " + backup)
                            if previousItem == "":
                                previousItem = processText
                                backup = previousItem
                            else:
                                backup = previousItem
                                previousItem = processText
                                itemChanged = True

                    if itemChanged:
                        if debug: print("DO CHECK")

                        for subsectionNo in range(len(jsonDict["Meeting"]["subsection"])):
                            for itemNo in range(len(jsonDict["Meeting"]["subsection"][subsectionNo]["Items"])):
                                #if debug: print("Compare: " + str(backup) + " To: " + str(jsonDict["Meeting"]["subsection"][subsectionNo]["Items"][itemNo]["index_in_pdf"]))
                                if jsonDict["Meeting"]["subsection"][subsectionNo]["Items"][itemNo]["index_in_pdf"] == backup:
                                    jsonDict["Meeting"]["subsection"][subsectionNo]["Items"][itemNo]["text"] = appendText
                                    if debug: print("Success: Added Notes to Item No. " + str(backup))

                        itemChanged = False

                    if text == "" or text == " " or text == " \n" or text == "\n":
                        pass
                    else:
                        appendText.append(text)
                        #if debug: print("Text Appended!")

                 
    if debug: print("RETURNING")
    return jsonDict




#####################################
##########     isPDF    #############
# Checks if PDF. Not very good      #
# just checks if ".pdf"             #
#####################################
def isPDF(file):
    file1 = file.split(".",1)
    file1 = file1[1]

    if file1 == "pdf":
        print("SUCCESS: " + file + " is PDF")
        return True
    else:

        return False

#####################################
########## handleTitle  #############
# Creates name from meeting title   #
# and date of meeting.              #
#####################################
def handleTitle(title, date):
    title = title.replace(" ", "_")
    date = date.split(", ", 1)[1]
    date = date.replace(",", "")
    date = date.replace(" ", "_")
    title = title + "_" + date
    return title

#####################################
########## main program #############
#####################################

print("PDF Scraper Started \n\n")



data = json.loads(jsonDict)

#TODO: Get filePath from Command Arguments
filePath = "2013" #Path to File

### Dissecting the Approved Minutes ###

# For each file in the
for file in os.listdir(filePath):
    current = os.path.join(filePath, file)
    print("Current: " + current)
    if os.path.isfile(current):
        if isPDF(file):

            print("\nScrape: " + file)
            fileName = file.split(".",1)
            fileName = fileName[0] #Get a filename without .pdf
            '''
            fh = open(filePath + "/" + fileName + "2.txt", "w")
            output = convert(current)


            fh.write(output)
            fh.close()  # Save text stripped PDF
            '''
            #print("Saved: " + filePath + "/" + fileName + ".txt")
            print("file: " + filePath + "/" + fileName + ".txt")
            print("filename: " + fileName)

            jsonFilePath = "2013/OPEN_SESSION_AGENDA_September_25_2017/json_OPEN_SESSION_AGENDA_September_25_2017.txt"
            textFilePath = "2013/OPEN_SESSION_AGENDA_September_25_2017.txt"

            data = json.load(open(jsonFilePath))

            data = appendJSON(textFilePath, data)
            #data = appendJSON(filePath + "/" + fileName + ".txt", data, fileName)




            # Do renaming / reoganizing of files and folders based on new name. #
            #newName = handleTitle(data["Meeting"]["title"],data["Meeting"]["date"])


            '''
            if not os.path.exists(filePath + "/" + newName):
                os.makedirs(filePath + "/" + newName)

            os.rename(filePath + "/" + fileName + ".txt", filePath + "/" + newName + "/" + newName + ".txt")
            os.rename(filePath + "/" + fileName + ".pdf", filePath + "/" + newName + ".pdf")

            data["Meeting"]["filename"] = newName + ".pdf"

            with open(filePath + "/" + newName + "/json_" + newName + '.txt', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            

            print("JSON File for "+newName+" successfully created")
            print()
            
            '''

        else:
            print("FAILED: " + file + " is not pdf")
            pass
