#decorator exist to access methods as an attribute
#we can't set an attribute while it's a property 
#we should make it setter to set our data

class Human:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def Email(self):
        return f"{self.first}.{self.last}@email.com"
 
   @property
    def Fullname(self):
        return f"{self.first} {self.last}"

    @Fullname.setter
    def Fullname(self, name):
        self.first, self.last = name.split(" ")

h1 = Human('Mena', 'Aziz')

h1.Fullname = "John youssef"

print(h1.first)
print(h1.Email)
print(h1.Fullname)
