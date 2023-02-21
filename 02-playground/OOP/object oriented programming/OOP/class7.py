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

	def __add__(self , anotherPoint):
		return Point(self.x + anotherPoint.x , self.y + anotherPoint.y)


point1 = Point(-5 , 10)
point2 = Point(15 , 20)


print(point1 , point2)
print(point1 + point2)
