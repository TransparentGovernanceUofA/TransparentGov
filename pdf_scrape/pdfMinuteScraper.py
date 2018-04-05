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
from datetime import datetime

debug = True
dateFormat = ""

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
def convertJSON(filePath, jsonDict, fileName):

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
    localItemNumber = 0
    textAcc = []
    motionText = []
    isCarried = False
    discussionStarted = False
    discussionAdded = False
    motionStarted = False
    afterWhiteSpace = 0

    pageNumber = 0
    appendString = []
    for text in binaryFile:
        lineNumber = lineNumber + 1
        text = text.rstrip()

        '''
        if text == "":
            continue
        '''
        # Append basic meeting information found in same place everytime.
        ## TODO: Make dynamic.

        if afterWhiteSpace < 5:
            if text == "":
                #print("TRiggered")
                continue
            else:
                afterWhiteSpace += 1
                #print("Whitespace: (" + str(text) + ")")
                if afterWhiteSpace == 1:
                    jsonDict["Committee"] = str(text).rstrip()
                    if debug: print("Committee: " + str(text).rstrip())
                elif afterWhiteSpace == 2:
                    jsonDict["Title"] = text.rstrip()
                    if debug: print("Title: " + str(text).rstrip())
                elif afterWhiteSpace == 3:
                    jsonDict["Date"] = text.rstrip()
                    if debug: print("Date: " + str(text).rstrip())
                    dateFormat = jsonDict["Date"].replace(",", "")
                    dateFormat = dateFormat.split(" ")
                    dateFormat = dateFormat[2] + "-" + dateFormat[1] + "-" + dateFormat[3]
                    dateFormat = datetime.strftime(datetime.strptime(dateFormat, '%d-%B-%Y'), '%Y-%m-%d')

                elif afterWhiteSpace == 4:
                    jsonDict["Location"] = text.rstrip()
                    if debug: print("Location: " + str(text).rstrip())
                elif afterWhiteSpace == 5:
                    jsonDict["Time"] = text.rstrip()
                    if debug: print("Time: " + str(text).rstrip())

        else: # Do these comparisons when lineNumber >= 65

            # Return if no more preprogrammed sections
            if subsectionNumber > len(splitStrings)-2:
                print("Returning Dict")
                return jsonDict

            # Check if the preprogrammed section is in the text
            if splitStrings[subsectionNumber+1] in str(text):
                startedBool = True
                subsectionNumber = subsectionNumber + 1
                #if debug: print("SUBSECTION NUMBER: " + str(subsectionNumber))
                localItemNumber = 0
                '''
                if subsectionNumber > 0:

                    #Build additional subsections
                    if debug: print("+ Section (" + str(subsectionNumber) + ")")

                    jsonDict["Meeting"]["subsection"].append({"sub_Title": None, "Items": [{"index_in_pdf": None,
                          "separate_index":None, "item_title":None, "pages_start":None, "pages_end":None, "text":None,
                          "presenters": [ { "name":None } ], "motions": [{ "motion":None, "carried":None, "content":None }],
                          "keywords": [ None, None ], "discussion":None, "purpose":None }]})

                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Title"] = splitStrings[subsectionNumber]

                    #if debug: print("Appending Items for " + str(splitStrings[subsectionNumber]))
                    #jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["text"] = appendString
                    #appendString = []

                else: # On the first time, just append title.
                    jsonDict["Meeting"]["subsection"][subsectionNumber]["Title"] = splitStrings[subsectionNumber]
                    
                '''
            else:
                if startedBool:

                    if str(text) == "\n":
                        pass
                    elif str(text) == " \n":
                        pass

                    else:
                        appendString.append(str(text).rstrip())
                        if (subsectionNumber > 0):
                            if debug: print(str(lineNumber) + " || " + splitStrings[subsectionNumber + 1] + "::" + str(text))

                if "Page" in text:
                    pageText = text.split("Page ")
                    #if debug: print("New Page! Page: " + str(pageText[1]))
                    pageNumber = int(pageText[1])
                    continue


                pattern = re.compile("\d\.")
                pattern2 = re.compile("\d\d\.")

                # Pattern for matching item numbers "Number + dot (.)"
                if pattern.match(text) != None or pattern2.match(text) != None:
                    itemNumber += 1  # Matching matches
                    localItemNumber += 1
                    number = text.split(".",1)
                    title = number[1]
                    number = number[0]
                    discussionStarted = False

                    # Append Additional Item to JSON format.
                    # TODO: HANDLE MULTIPART ITEM TITLE
                    if debug: print("+ ITEM ("+title+") | Subsection Number: " + str(subsectionNumber) + " Item Number: " + str(itemNumber))
                    jsonDict["Items"].append({"Item No.": "N/A",
                                              "Agenda Title": "N/A",
                                              "Motion": "N/A",
                                              "Action Requested": "Approval",
                                              "Date": "N/A",
                                              "Committee": "N/A",
                                              "Proposed By": "N/A",
                                              "Presenter": "N/A",
                                              "Description": "N/A",
                                              "Participation": [ "N/A" ],
                                              "Approval Route": [ "N/A"],
                                              "Final Approver": "N/A"
                                            })

                    if localItemNumber > 1:  # Append discussion text
                        #if debug: print("Subsection Number: " + str(subsectionNumber) + " Item Number: " + str(itemNumber) + " Local Item Number: " + str(localItemNumber))
                        if discussionAdded:
                            jsonDict["Items"][itemNumber]["Description"] = " ".join(textAcc)
                            if debug: print("### We have appended your discussion")
                            discussionAdded = False

                    textAcc = []  # Reset Discussion Text

                    jsonDict["Items"][itemNumber]["Item No."] = str(number)
                    jsonDict["Items"][itemNumber]["Date"] = dateFormat
                    jsonDict["Items"][itemNumber]["Committee"] = "GFC"
                    #jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][localItemNumber]["pages_start"] = str(pageNumber)
                    jsonDict["Items"][itemNumber]["Agenda Title"] = title

                    #TODO: HANDLE PAGES END
                    #jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][localItemNumber-1]["pages_end"] = str(pageNumber)


                # String comparisons unique to "Opening Minuets"
                if subsectionNumber == 0:
                    # Append all Attendees not on StopWord List
                    if text.rstrip() not in nonAttendance:
                        jsonDict["Attendees"].append(str(text))
                        if debug: print("Appended Attendee: " + str(text))
                    else:
                        #if debug: print("Rejected; " + text)
                        pass

                # String comparisons unique to "Discussion Minuets"

                if subsectionNumber >= 1:

                    if "Presenter(s)" in text:
                        newText = text.strip("Presenter(s): ")

                        jsonDict["Items"][itemNumber]["Presenter"] = newText
                        if debug: print("Presenter detected and assigned: " + newText)

                    elif "Purpose of the Proposal:" in text:
                        newText = text.strip("Purpose of the Proposal: ")
                        #jsonDict["Items"][itemNumber]["Purpose"] = newText
                        if debug: print("Purpose detected and assigned: " + newText)

                    elif "Motion:" in text:
                        discussionStarted = False
                        if debug: print("Motion Detected!")
                        newText = text.split(':')
                        newText = newText[1]
                        if debug: print("Motion Title: " + newText)
                        jsonDict["Items"][itemNumber]["Motion"] = str(newText)
                        isCarried = True

                    elif "THAT" in text:
                        jsonDict["Items"][itemNumber]["Action Requested"] = text
                        if debug: print("Motion Content: " + text)

                    if isCarried == True:
                        if "CARRIED" in text:
                            jsonDict["Items"][itemNumber]["Approval Route"].append(jsonDict["Committee"] + " CARRIED")
                            isCarried = False
                            if debug: print("Motion Carried: " + "True")

                    pattern3 = re.compile("Motion \D")
                    if pattern3.match(text) != None:
                        discussionStarted = False
                        motionStarted = True
                        manipulatedString = text.split(":")
                        manipulatedString = manipulatedString[1]
                        jsonDict["Items"][itemNumber]["Motions"] = manipulatedString

                        if debug: print("+ MOTION (" + manipulatedString + ")")

                    #TODO: Handle Multiple Motions
                    if motionStarted == True:

                        if "CARRIED" in text:
                            if debug: print("CARRIED SUCCESS")

                            jsonDict["Items"][itemNumber]["Approval Route"].append(jsonDict["Committee"] + " CARRIED")
                            #jsonDict["Meeting"]["subsection"][subsectionNumber]["Items"][itemNumber]["motions"][0][
                            #    "content"] = motionText
                            motionText = []
                            motionStarted = False

                        else:
                            motionText.append(text)
                            if debug: print("Motion text appended")

                        #itemNumber = int(text.strip("."))

                    if "Discussion:" in text:
                        discussionStarted = True
                        continue

                    if discussionStarted:
                        if debug: print("Appending Line to Discussion")
                        discussionAdded = True
                        textAcc.append(text)

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





#TODO: Get filePath from Command Arguments
filePath = "2013" #Path to File

### Dissecting the Approved Minutes ###

# For each file in the
for file in os.listdir(filePath):
    current = os.path.join(filePath, file)
    print("Current: " + current)
    if os.path.isfile(current):
        if isPDF(file):

            print("\n Scrape: " + file)
            fileName = file.split(".",1)
            fileName = fileName[0] #Get a filename without .pdf

            fh = open(filePath + "/" + fileName + ".txt", "w")
            output = convert(current)

            data = json.loads(jsonDict3)

            fh.write(output)
            fh.close()  # Save text stripped PDF

            #print("Saved: " + filePath + "/" + fileName + ".txt")
            data = convertJSON(filePath + "/" + fileName + ".txt", data, fileName)

            dateFormat = data["Date"].replace(",", "")
            dateFormat = dateFormat.split(" ")
            dateFormat = dateFormat[2] + "-" + dateFormat[1] + "-" + dateFormat[3]
            dateFormat = datetime.strftime(datetime.strptime(dateFormat, '%d-%B-%Y'), '%Y-%m-%d')

            # Do renaming / reoganizing of files and folders based on new name. #
            newName = handleTitle(data["Title"],data["Date"])

            if not os.path.exists(filePath + "/" + newName):
                os.makedirs(filePath + "/" + newName)

            if not os.path.exists(filePath + "/" + "JSON"):
                os.makedirs(filePath + "/" + "JSON")


            if not os.path.exists(filePath + "/static/GFC/" + dateFormat):
                os.makedirs(filePath + "/static/GFC/" + dateFormat)

            os.rename(filePath + "/" + fileName + ".txt", filePath + "/" + newName + "/" + newName + ".txt")


            os.rename(filePath + "/" + fileName + ".pdf", filePath + "/" + "static/GFC/" + dateFormat + "/Approved-Minutes.pdf")

            data["url"] = "/static/GFC/" + dateFormat + "/Approved-Minutes.pdf"
            print("URL : " + str(data["url"]))

            with open(filePath + "/" + "JSON" + "/json_GFC_" + dateFormat + '_Approved_Minuets.txt', 'w') as outfile:
                json.dump(data, outfile, indent=4)

            print("JSON File for "+newName+" successfully created")
            print()

        else:
            print("FAILED: " + file + " is not pdf")
            pass

