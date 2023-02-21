from random import randrange
class Benghalokh:

	intellegence = 0
	boredom = 0
	interestings = ['Football']
	def __init__(self, name, age, skin):
		self.name = name 
		self.age = age
		self.skin = skin
		self.interestings = self.interestings[:]
		self.intellegence = self.intellegence

	def __str__(self):
		return 'I\'m {}, {} years and I\'m {} now.'.format(self.name.title() , self.age , self.interestings)


	def time(self):
		intellegence += 1 
		boredom += 1

	def state(self):
		if self.intellegence <= intellegence and self.boredom <= boredom:
			



karkor = Benghalokh('karkor' , 21 , 'Brown')

print(karkor)