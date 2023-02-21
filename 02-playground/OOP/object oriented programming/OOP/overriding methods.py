#Overriding methods ..

class Book:

	def __init__(self , name , author):
		self.name = name 
		self.author = author

	def say(self):
		print('say')

	def __str__(self):
		return '{} by {}'.format(self.name , self.author.title())

class PaperBook(Book):

	def __init__(self , name , author, NumPages):
		Book.__init__(self , name , author)
		self.NumPages = NumPages

class Ebook(Book):

	def __init__(self , name , author , size):
		Book.__init__(self, name , author)
		self.size = size
	def say(self):
		print('hey')
		#Book.say(self)
		super().say() #>>> Important .. if we want to call say() in Ebook class and in Book class as well

class Library(Book):
	def __init__(self):
		self.books =[]

	def addBook(self , book):
		self.books.append(book)

	def getNumBooks(self):
		return str(len(self.books)) + ' books in the library class!'



myPaperBook = PaperBook('7 Habits' , 'mina' , 500)
myEBook = Ebook('Succes' , 'O\'REALLY' , 2)
myEBook.say() #overriding method
print(myPaperBook.name)
print(myPaperBook)
print(myEBook.name)
print(myEBook)
addl = Library()
addl.addBook(myPaperBook)
addl.addBook(myEBook)
print(addl.getNumBooks())	