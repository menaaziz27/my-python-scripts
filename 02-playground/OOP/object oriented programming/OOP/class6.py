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


point1 = Point(5,6)

print(point1)


