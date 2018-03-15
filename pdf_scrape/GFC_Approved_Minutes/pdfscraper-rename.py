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
import os, glob

def convert(fname, pages=None):
	if not pages:
		pagenums = set()
	else:
		pagenums = set(pages)

	output = StringIO()
	manager = PDFResourceManager()
	converter = TextConverter(manager, output, laparams=LAParams())
	interpreter = PDFPageInterpreter(manager, converter)

	infile = open(fname, 'rb')
	for page in PDFPage.get_pages(infile, pagenums):
		interpreter.process_page(page)
	infile.close()
	converter.close()
	text = output.getvalue()
	output.close
	
	return text


def parse(fileName):
	lineCount = 0
	pageCount = 0
	i= 0
	with open(fileName,'rb') as file:
		for text in file:
			# Line Count to show progress
			lineCount = lineCount + 1
			if (lineCount % 23 == 0): #23 lines/page at 12pt font
				pageCount = pageCount + 1
				print("Pages Printed: "+str(pageCount))			
			# Read lines
			if keywords[i] in text:
				i = i + 1
				print("i: "+str(i-1)+"|"+str(keywords[i-1]))
			if i > 0:
				filePointers[i-1].write(text)	
	
print("OS Renamer \n")

for filename in os.listdir("."):
	output = convert(filename)
	fh = open(filename+".txt","wb")
	output = output.encode('utf-8').strip()
	fh.write(output)
	fh.close()
	
	

# Define deliniators 
keywords = []
filePointers = []

splitNames = ["ATTENDEES","OPENING_SESSION","DISCUSSION_ITEMS", "ACTION_ITEMS", "QUESTION_PERIOD", "INFORMATION_REPORTS", "CLOSING_SESSION"]

splitStrings = ["ATTENDEES","OPENING SESSION","DISCUSSION ITEMS", "ACTION ITEMS", "DISCUSSION ITEMS", "INFORMATION REPORTS", "CLOSING SESSION"]
numberSplit = len(splitStrings)

# Create Files for each individual thing
i = 0
while (i < numberSplit):
	keywords.append(splitStrings[i].encode('utf-8'))
	fp = open(fileName + "_" + splitNames[i], 'wb')
	filePointers.append(fp)
	#print(str(splitNames[i])+" Pointer i: "+str(i))
	i = i + 1

keywords.append(splitStrings[0].encode('utf-8')) #Add an extra


parse("scrapeTest.txt")
			
# Close files
for file in filePointers:
	#print("Closing: " + str(file))
	file.close()
print()	
print(fileName + " is finished being processed")
