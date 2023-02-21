class Aquatic:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"{self.name} of the sea"

class Ambulatory:
    def __init__(self, name):
        self.name = name
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"{self.name} of the land"

class penguin(Ambulatory,Aquatic):
    def __init__(self,name):
        super().__init__(name)

captain_cook = penguin("lola")
print(captain_cook.name)
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())
# print(help(penguin))
# print(penguin.mro())
print(penguin.__mro__)