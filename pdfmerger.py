import PyPDF2
import sys
import os 
print(dir (PyPDF2))
merger=PyPDF2.PdfMerger()
for file in os.listdir(os.curdir):#curdir it mean current directory
    if file.endswith(".pdf"):
        
        merger.append(file)
    merger.write("combinedpdf.pdf")
    
