#second example of polymorphism
#the same operation works for different kinds of objects
#like 2 + 8 = 4
#but "2" + "8" = "28"
#and this is done by polymorphism

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}."

    def __len__(self):
        return self.age

    def __add__(self,other):
        if isinstance(other,Human):
            return Human(first = "newBorn", last = self.last, age = 0) #XXX
        return "can't add"

    def __mul__(self,other):
        if isinstance(other,int):
            return [self for i in range(other)]
        return "cam't multiply"

j = Human('jenny', 'larrson', 50)
k = Human('mark', 'jones' , 60)
print(j + k)
print(j * 2)
