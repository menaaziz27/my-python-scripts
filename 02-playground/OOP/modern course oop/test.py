class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Getx(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(15,25)

print(p1.Getx())
print(p1.getY())

print(p1)