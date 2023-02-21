cityNames = ['Detroit' , 'Ann Arbor' , 'Pittsburgh' , 'Mars' , 'New York']
population = [333214 , 124555 , 673276 , 636312,854753]
states = ['MI' , 'MI' , 'PA' , 'PA' , 'NY']

city_tuples = zip(cityNames,population,states)

class City:
	def __init__(self , n , p , s):
		self.name = n
		self.population = p
		self.state = s

	def __str__(self):
		return '{}, {} (pop: {})'.format(self.name, self.state, self.population) # these are the names of our defined attributes

#for n,p,s in city_tuples:
#	print(n,p,s)

#cities = []
#
#for city_tup in city_tuples:
#	name , pop , state = city_tup
#	city = City(name , pop , state) # instance of the city class
#	cities.append(city)
#	#print(city)
#
#print(cities)

cities = [City(n,p,s) for (n,p,s) in city_tuples]
print(cities)