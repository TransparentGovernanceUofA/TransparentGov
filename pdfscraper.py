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
	
fileName = 'Approved-Minutes-GFC-NO-27'
pdfName = fileName + '.pdf'
output = convert(pdfName)

fh = open("scrapeTest.txt","wb")
output = output.encode('utf-8').strip()
fh.write(output)

fh.close()


#print("Done conversion to text")



f = open("scrapeTest.txt",'rb')

keywords = []
filePointers = []

splitStrings = ["ATTENDEES","OPENING SESSION","DISCUSSION ITEMS", "ACTIONS ITEMS", "DISCUSSION ITEMS", "INFORMATION REPORTS", "CLOSING SESSION"]
numberSplit = len(splitStrings)
print(numberSplit)

i = 0
while (i < numberSplit):
	keywords.append(splitStrings[i].encode('utf-8'))
	fp = open(fileName + "_" + splitStrings[i], 'ab')
	filePointers.append(fp)
	print("File Pointer i: "+str(i))
	i = i + 1


sys.stdout.write('Made it this far\n')
sys.stdout.flush()

lineCount = 0

while f.readline():
	lineCount = lineCount + 1
	if (lineCount % 23 == 0):
		print("Lines Printed: "+str(lineCount))
	
	text = f.readline()
	for keyword in keywords:
		if keyword in text:
			i = i - 1
			print(keyword)
	if i <= 6:
		filePointers[i].write(text)

print("Close")
for file in filePointers:
	file.close()
	
print("Done")