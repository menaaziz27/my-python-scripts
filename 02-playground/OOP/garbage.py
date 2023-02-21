from random import randrange

class Pets:
	boredom_decreament = 4
	hunger_decreament = 6
	hunger_threshold = 10
	boredom_threshold = 5
	sounds = ['wrrp']

	def __init__(self, name = 'Kitty'):
		self.name = name
		self.boredom = randrange(self.boredom_threshold)
		self.hunger = randrange(self.hunger_threshold)
		self.sounds = self.sounds[:]
	
	def __str__(self):
		state = "Im " + self.name +'. '
		state += "I'm " + self.mood() + ' now.'
		return state

	def clock_tick(self):
		self.boredom += 1
		self.hunger += 1

	def hi(self):
		print(self.sounds[randrange(len(self.sounds))])
		self.reduce_boredom()

	def teach(self, word):
		self.sounds.append(word)
		self.reduce_boredom()

	def feed(self):
		self.reduce_hunger()

	def mood(self):
		if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
			return "Happy"
		elif self.hunger > self.hunger_threshold:
			return 'Hungry'
		else :
			return'bored'

	def reduce_boredom(self):
		self.boredom = max(0 , self.boredom - self.boredom_threshold)

	def reduce_hunger(self):
		self.hunger = max(0 , self.hunger - self.hunger_threshold)


class Cats(Pets):
	sounds = ['Meow'] 

	#def __init__(self , name = 'kitty'):
	#	self.nails = 'yes'  		>>> lw hn3arraf constructor hena kman .. lw 3yzen nst5dm 7aga mn el constructor elli fo2eh yb2a lazm n3mello inheret .. lkn law msh 3ayzen nst5dm 7aga mn el super class n3ml el constuctor bta3o hwa lwa7do 3ady
	#kda e7na law 2olna pet.sounds hytl3lna el sounds bta3 el Cats class 
#msh lazm kol class yb2a feh constructor X
#hena 3amlen inheritance w el constructor elli bnst3mlo bta3 el super class fo2 
	def Chasing_rats(self):
		return 'What are you doing, Pinky? Taking over the world?!'


cat = Cats()

print(cat.sounds)
print(cat.hunger)
print(cat.boredom)	
print(cat)	
'''pet = Pets('Fido')

print(pet.hunger)
print(pet.boredom)
for i in range(10):
	pet.clock_tick()
	print(pet)

pet.hi()
pet.teach('jerr')
pet.teach('AAA')
pet.teach('Meow')
for i in range(5):	
	pet.hi()

print(pet)

for i in range(10):
	pet.clock_tick()
	print(pet)
#print(pet.hunger)
#print(pet.boredom)
#print(pet)
'''