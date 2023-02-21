class Point():
    def __init__(self, intX, intY):
        self.x = intX
        self.y = intY
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
point1 = Point(6,7)

print(point1.distanceFromOrigin())
