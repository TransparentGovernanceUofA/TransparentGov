'''
import pdfquery
pdf = pdfquery.PDFQuery("pdfs/Combined-agenda-and-documents.pdf")
pdf.load()

pdf.tree.write('test.xml', pretty_print=True)
'''
# Adapted from https://reachtim.com/articles/PDF-Manipulation.html
# Updated to python 3 by Austin Crapo
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

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
	
output = convert('pdfs/Combined-agenda-and-documents.pdf', pages=[0,1,2,3,4,5])

fh = open("test.txt","w")
fh.write(output)
fh.close()
