#Sorting a list of instances 

class Fruit:

	def __init__(self , name , price):
		self.name = name
		self.price = price

	def sorted_priority(self):
		return self.price


L = [
	 Fruit('Cherry' , 10),
	 Fruit('Apple' , 5),
	 Fruit('Blueberry' ,20)
	 ]

#print(sorted(L , key = Fruit.sorted_priority))
for f in sorted(L , key = Fruit.sorted_priority):
	print(f.name)