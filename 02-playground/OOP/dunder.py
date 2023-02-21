class Point:
	def __init__(self, x , y ):
		self.x = x 
		self.y = y

	def __str__(self):
		return 'point ({} , {})'.format(self.x, self.y)

	def __add__(self , otherpoint): 		#hena bn-create instance bs msh bn7otto f variable
		return Point(self.x + otherpoint.x,
					 self.y + otherpoint.y)

	def __sub__(self , otherpoint):			#hena bn-create instance bs msh bn7otto f variable
		return Point(self.x - otherpoint.x,
					 self.y - otherpoint.y)

	def halfway(self , target):				#hena bn-create instance mn el class w bn7otto f variable mid 
		mx = (self.x + target.x) / 2 
		my = (self.y + target.y) / 2
		return Point(mx , my)

p1 = Point(10,5)
p2 = Point(6, 3)
mid = p1.halfway(p2) #important
print(mid)
print(mid.__dict__)
print(p1)
print(p2)
print(p1 + p2)
print(p1 - p2)
