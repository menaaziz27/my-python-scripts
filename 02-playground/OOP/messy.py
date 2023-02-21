class Persons:

	knowledge = ['Talk' , 'Walk']
	grades = 0
	Calories = 2000
	def __init__(self , name , age, nationality):
		self.name = name
		self.age = age
		self.nationality = nationality
		self.knowledge = self.knowledge[:]

	def learn(self):
		self.grades += 1
		print('My grades are increased!')

	def hungry(self):
		self.Calories += 200
		print('My Calories are increased lol.')

	def workout(self):
		print('I\'m burning calories')
		print('Calories are decreased!')
		self.Calories -= 100

	def __str__(self):
		return 'I\'m {} {} years \nmy nationality : {}\ngrades : {}\ncalories : {}\nknowledge : {}\n-----------------------'.format(
			self.name,
			self.age, 
			self.nationality,
			self.grades,
			self.Calories,
			self.knowledge
			)

class Student(Persons):


	knowledge = ['physics' , 'chemistry' , 'english']
	Calories = 1500

	def __init__(self, name , age , nationality , id):
		Persons.__init__(self , name , age , nationality)
		self.id = id

	def learn(self , subject):       #overridded metod with extra parameter kman 
		super().learn()
		print('My knowledge is increased too!')
		self.knowledge.append(subject)
		return 'grades : {} , Knowledge : {}.'.format(self.grades , self.knowledge)



# stu = Student('hema' , 20 , 'Egy' , 80020234)

# print(stu)
# print(stu.learn('Arabic'))
# stu.hungry()
# print(stu.Calories)


# per = Persons('mina' , 22 , 'Aus')
# print(per)
