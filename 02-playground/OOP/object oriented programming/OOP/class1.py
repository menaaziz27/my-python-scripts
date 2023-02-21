class Point():
    def __init__(self, n1, n2):
        self.x = n1
        self.y = n2
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
point1 = Point(5,6)
point2 = Point(10,100)

print(point1.getX())
print(point1.getY())
print(point2.getX())
print(point2.getY())