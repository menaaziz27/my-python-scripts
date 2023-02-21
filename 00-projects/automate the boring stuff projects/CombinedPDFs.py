import PyPDF2

pdfFile = open ('C:\\Users\\3azzouz\\mypythonscripts\\meetingminutes1.pdf','rb')
pdf2File = open('C:\\Users\\3azzouz\\mypythonscripts\\meetingminutes2.pdf','rb')
reader1 = PyPDF2.PdfFileReader(pdfFile)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

	
for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

	
outputFile = open('Combinedminutes.pdf','wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdf2File.close()