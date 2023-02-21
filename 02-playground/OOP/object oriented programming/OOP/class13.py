#Inheritance ..

from random import randrange

class Pet():

    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']

    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


class Cats(Pet):

	sounds = ['Meow']

	def chasing_rats(self):
		return 'What are you doing, Pinky? Taking over the world?!'




class Cheshire(Cats):
		 # this inherits from Cat, which inherits from Pet

	def smile(self): # this method is specific to instances of Cheshire
		print(":D :D :D")



class savannah(Cats):

	sounds = ['gherr']

	def savannah_talks(self):
		return 'Savannah is here, gherr!'




class Bird(Pet):
	sounds = ['chirp']

	def __init__(self , name ,chirp_number = 2):
		Pet.__init__(self , name )
		self.chirp_number = chirp_number

# b1= Bird('Tweety', 5)
# print(b1.sounds)
# sav = savannah('Toyger')

# print(sav.hunger)
	


# Cheshire_Instance = Cheshire("Cheshire")
# Cheshire_Instance.hi()
# print(Cheshire_Instance)

cat = Cats('marla')
print(cat)
cat.teach('adragdabra')
print(cat.sounds)
bir = Bird('bird')
# print(bir.chirp_number)
# cat.hunger_threshold = 5
# print(cat.hunger_threshold)
# cat2 = Cats()
# print(cat2.hunger_threshold)

# chesh = Cheshire('karla')
# print(chesh.sounds)