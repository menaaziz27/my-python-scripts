class point:
	def getx(self):
		return self.x

p = point()
p.x = 5

p.getx = 50
print(p.getx)