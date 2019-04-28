import re
from docx import Document

doc = Document('D:/Java.docx')

for p in doc.paragraphs:
    print(p)
