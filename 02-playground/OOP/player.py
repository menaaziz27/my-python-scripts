from random import  randrange
import random
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
					random.choice(MadridList).tackling(self)
				else:
					random.choice(BarcaList).tackling(self)
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
		self.goal = randrange(2)
		if self.goal == 1:
			print('goal')
		else:
			print('saved')

	def train(self):
		self.power += 5
		self.stamina += 2
		print('My power increased by 5!')
		print('My stamina increased by 2!')

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

	def __init__(self,name, age , power ,stamina, Nationality):
		player.__init__(self, name, age, power)
		self.Nationality = Nationality
		self.stamina = stamina



class Madrid(player):
	Team = 'Real Madrid'
	Coach = 'Zidan'
	Training_Time = '10 am'

	def __init__(self,name, age , power ,stamina, Nationality):
		player.__init__(self, name, age, power)
		self.Nationality = Nationality
		self.stamina = stamina




BarcaList = []
Messi = Barca('Messi', 32, 99, 90, 'Argentine')
Suarez = Barca('Suarez', 34, 92, 98, 'uruguai')
BarcaList.append(Messi)
BarcaList.append(Suarez)

MadridList = []
Ronaldo = Madrid('CR7', 33, 97,92, 'portugese')
Benzema = Madrid('Benzema', 31 , 95 , 93,  'France')
MadridList.append(Ronaldo)
MadridList.append(Benzema)

MadridList[0].train()
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
Messi.Pass(Suarez)
print('successful pass :', Messi.successful_passing)
print('number of touches :',Suarez.num_of_touches)
print(player.Lastonetouchedball)
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