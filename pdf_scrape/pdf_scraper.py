import pdfquery
pdf = pdfquery.PDFQuery("pdfs/Combined-agenda-and-documents.pdf")
pdf.load()

pdf.tree.write('test.xml', pretty_print=True)