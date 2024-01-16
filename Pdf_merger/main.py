import PyPDF2
import os

print(os.getcwd())

pdfiles = ["Pdf_merger/1.pdf","Pdf_merger/2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
pdfFile.close()
merger.write('Pdf_merger/merged.pdf')