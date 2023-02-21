>>> import PyPDF2
>>> PDF = open('C:\\Users\\3azzouz\\mypythonscripts\\meetingminutes1.pdf' , 'rb')
>>> reader = PyPDF2.PdfFileReader(PDF)
>>> reader.numPages
19
>>> page = reader.getPage(0)
>>> page.extractText()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '

#to extract all text in all pages in PDF ..

>>> for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())


#To combine two PDF files ..
