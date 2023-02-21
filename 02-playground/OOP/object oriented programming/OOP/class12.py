Current_Year = 2020

class Person:
	def __init__(self , name , year_born):
		self.name = name
		self.year_born = year_born

	def getAge(self):
		return (Current_Year - self.year_born)

	def __str__(self):
		return '{} has ({})'.format(self.name , self.getAge())

class Student(Person):
	def __init__(self, name , year_born):
		Person.__init__(self,name,year_born)
		self.Knowledge = 0

	def study(self):
		self.Knowledge += 1

Alice = Student('Alice' , 1999)
Alice.study()
print(Alice.Knowledge)
print(Alice)
print(Alice.getAge())