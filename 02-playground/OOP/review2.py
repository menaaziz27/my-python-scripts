class Fruit:
	def __init__(self , name , price):
		self.name = name 
		self.price = price

	def sorting_priority(self):
		return self.price



l = [
	Fruit('apple' , 10),
	Fruit('cherry' , 5),
	Fruit('banana' , 20)
	]

for f in sorted(l , key = Fruit.sorting_priority):	#Fruit.sorted_priority de elli hya lma n-access class method aw class variable f lazm 3n tre2 el class name aw instance name 
	print(f.name)