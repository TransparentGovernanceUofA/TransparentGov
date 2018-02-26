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
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys
import os

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
        with open(path + "/" + fname, 'rb') as infile:
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


def processFile(fileName):
    filePointers = []
        fileName = fileName.split(".",1)
        fileName = fileName[0]
        output = convert(fileName + ".pdf")
        print()
        fh = open(path + "/" + fileName + ".txt","wb")
        output = output.encode('utf-8').strip()
        fh.write(output)
        fh.close() #Save text stripped PDF
        
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

# Define deliniators 
newName = ""
keywords = []
filePointers = []

splitNames = ["ATTENDEES","OPENING_SESSION","DISCUSSION_ITEMS", "ACTION_ITEMS", "QUESTION_PERIOD", "INFORMATION_REPORTS", "CLOSING_SESSION"]

splitStrings = ["ATTENDEES","OPENING SESSION","DISCUSSION ITEMS", "ACTION ITEMS", "DISCUSSION ITEMS", "INFORMATION REPORTS", "CLOSING SESSION"]
numberSplit = len(splitStrings)

print("Begin Approved-Minutes Scraper \n")

path = "2013"

for file in os.listdir(path):
    current = os.path.join(path, file)
        if os.path.isfile(current):
            print("Compare " + file)
                if isPDF(file):
                    print("Processing: " + file)
                        processFile(file)
                else:
                    print(file + ": failed")


#fileName = 'Approved-Minutes'


print()	
print("Done.")
