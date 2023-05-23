from pdf2docx import Converter

pdf = input("Caminho do PDF: ")
docx = "document.docx"

cv = Converter(pdf)
cv.convert(docx)