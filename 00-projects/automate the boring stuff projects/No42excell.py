>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> wb.active    #de hya hya eli t7t
<Worksheet "Sheet1">
>>> wb.sheetnames
['Sheet1', 'Sheet2', 'Sheet3']
>>> wb['Sheet1'] #la7z en de hya hya elli fo2 
<Worksheet "Sheet1">

>>> sheet = wb.active
>>> cell = sheet.cell(row=1 , column=1)
>>> print(cell.value)
2015-04-05 13:34:02
>>> cell = sheet['B2']
>>> print(cell.value)
Cherries
>>> cell = sheet['C3']
>>> print(cell.value)
14
>>> 
>>> for i in range(1,8):
	print(i,sheet.cell(row=i,column=2).value)

	
1 Apples
2 Cherries
3 Pears
4 Oranges
5 Apples
6 Bananas
7 Strawberries
>>> 


""" To crete excell file and modify it """
>>> import openpyxl
>>> wb = openpyxl.Workbook()
>>> wb
<openpyxl.workbook.workbook.Workbook object at 0x038990E8>
>>> wb.sheetnames
['Sheet']

>>> sheet = wb['Sheet']
>>> sheet
<Worksheet "Sheet">
>>> sheet['A1'].value == None
True
>>> sheet['A1'] = 42
>>> sheet['A2'] = 'Hello'
>>> wb.save('ex.xlsx')

>>> wb.create_sheet() #To create a new sheet
<Worksheet "Sheet1">
>>> Sheet1 = wb.create_sheet()
>>> Sheet1
<Worksheet "Sheet2">
>>> wb.sheetnames
['Sheet', 'Sheet1', 'Sheet2']
>>> wb.save('ex.xlsx')

>>> wb.sheetnames[0]
'Sheet'

>>> sheet1 = wb['Sheet']
>>> sheet1.title = 'Fruit' #to rename a sheet
>>> wb.save('ex.xlsx')

>>> wb.create_sheet(index = 0 , title='My first sheet') # if we wanna create a new sheet with a specific location
<Worksheet "My first sheet">
>>> wb.save('ex.xlsx')

