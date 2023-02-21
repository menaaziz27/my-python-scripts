class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def __str__(self):
		return 'Point ({},{})'.format(self.x,self.y)

	def halfway(self , target):
		mx = (self.x + target.x) // 2
		my = (self.y + target.y) // 2
		return Point(mx , my)


p1 = Point(3,4)
p2 = Point(5,12)

mid = p1.halfway(p2)

print(mid)