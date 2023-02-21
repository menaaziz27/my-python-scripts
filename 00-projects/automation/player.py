from random import  randrange
from random import choice

class player:

	Lastonetouchedball = 'None'

	def __init__(self, name, age , power ):
		self.name = name
		self.age = age 
		self.power = power
		self.num_of_touches = 0
		self.successful_passing = 0
		self.wrong_passing = 0
		self.goal = 0

	def Pass(self, receiver):
		if player.Lastonetouchedball == self.name or player.Lastonetouchedball == 'None':		 
			if randrange(2) == 1:
				print('missed pass')
				if self.Team == receiver.Team == 'Barcelona FC':
					choice(MadridList).tackling(self)
				else:
					choice(BarcaList).tackling(self)
			else:
				print('successful pass')	
				self.successful_passing += 1
				receiver.num_of_touches += 1
				receiver.BallNow()
		else:
			print("I can't pass")

	def tackling(self , player):
		print(self.name,'Took the ball from',player.name)
		player.wrong_passing += 1 
		self.num_of_touches += 1
		self.BallNow()

	def BallNow(self):
		player.Lastonetouchedball = self.name
		print('The ball now with', player.Lastonetouchedball)


	def kick(self):
		if randrange(2) == 1:
			print('Goal!!')
			self.goal += 1
			if self.Team == 'Barcelona FC':
				Barca.Score_Team += 1
			else:
				Madrid.Score_Team += 1
		else:
			print('saved')
			if self.Team == 'Barcelona FC':
				Madrid.saved_kicks += 1
			else:
				Barca.saved_kicks += 1

	def train(self):
		self.power += 1
		self.stamina += 1
		print('My power increased by 1!')
		print('My stamina increased by 1!')

	def resultNow(self, opponent):
		return '{} : {}'.format(self.goal, opponent.goal)


	def __str__(self):
		return 'Name : {}\nnationality : {}\nstamina : {}\npower: {}\nteam : {}\ncoach : {}\n'.format
		(
			self.name,
			self.Nationality,
			self.stamina,
			self.power,
			self.Team,
			self.Coach
		) 



class Barca(player):

	Team = 'Barcelona FC'
	Coach = 'Valverdi'
	Training_Time = '11 am'
	Score_Team = 0
	saved_kicks = 0
	def __init__(self,name, age , power ,stamina, Nationality):
		player.__init__(self, name, age, power)
		self.Nationality = Nationality
		self.stamina = stamina

	def train(self):
		self.power += 4
		self.stamina += 3

class Madrid(player):

	Team = 'Real Madrid'
	Coach = 'Zidan'
	Training_Time = '10 am'
	Score_Team = 0
	saved_kicks = 0

	def __init__(self,name, age , power ,stamina, Nationality):
		player.__init__(self, name, age, power)
		self.Nationality = Nationality
		self.stamina = stamina

	def train(self):
		self.power += 2
		self.stamina += 2


#Barcelona Team
BarcaList = []
Messi = Barca('Messi', 32, 99, 90, 'Argentine')
Suarez = Barca('Suarez', 34, 92, 98, 'uruguai')
BarcaList.append(Messi)
BarcaList.append(Suarez)

#Real Madrid Team
MadridList = []
Ronaldo = Madrid('CR7', 33, 97,92, 'portugese')
Benzema = Madrid('Benzema', 31 , 95 , 93,  'France')
MadridList.append(Ronaldo)
MadridList.append(Benzema)

# for i in range(10):
# 	Messi.Pass(Suarez)

#Kick method

# for i in range(5):
# 	Messi.kick()
# 	Suarez.kick()

# print('Messi goals', Messi.goal)
# print('Suarez goals ',Suarez.goal)
# print('Barcelona total goals',Barca.Score_Team)

#train method

# print('messi power :',Messi.power)
# print('messi stamina :' , Messi.stamina)
# print('CR7 power :',Ronaldo.power)
# print('CR7 stamina :', Ronaldo.stamina)
# for i in range (2):
# 	Ronaldo.train()
# 	Messi.train()
# print('After training 2 times ... ')
# print('messi power :',Messi.power)
# print('messi stamina :' , Messi.stamina)
# print('CR7 power :',Ronaldo.power)
# print('CR7 stamina :', Ronaldo.stamina)

#pass method


# Messi.train()
# print(Messi.power)
# print(Messi.stamina)
# Messi.train()
# print(Messi.power)
# print(Messi.stamina)
# Ronaldo.train()
# print(Ronaldo.power)
# print(Ronaldo.stamina)
# Ronaldo.train()
# print(Ronaldo.power)
# print(Ronaldo.stamina)
# MadridList[0].train()
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# Messi.Pass(Suarez)
# print('successful pass :', Messi.successful_passing)
# print('number of touches :',Suarez.num_of_touches)
# print(player.Lastonetouchedball)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Ronaldo.Pass(Benzema)
# Benzema.Pass(Ronaldo)
# Messi.Pass(Suarez)
# Suarez.Pass(Messi)
# print(Ronaldo.successful_passing)
# print(Benzema.num_of_touches)