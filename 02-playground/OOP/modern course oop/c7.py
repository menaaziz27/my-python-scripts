#second case to use class methods
#creating instances of the class

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @classmethod
    def set_instance(cls, str_data):
        first,last,age = str_data.split(",")
        return cls(first,last,int(age))

    def Birthday(self):
        return f"Happy {self.age}th birthday"
    
    def Full_name(self):
        return f"{self.first} {self.last}."

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."


usr1 = User.set_instance("Joe,smith,98")

print(usr1.first)
print(usr1.Full_name())
print(usr1.Birthday())