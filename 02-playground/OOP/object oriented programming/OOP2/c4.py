#class Variables first case to track something 
#attributes

class Person:
    active_Persons = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        Person.active_Persons += 1

    def log_out(self):
        Person.active_Persons -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f'{self.first} likes {thing}'

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

# print(Person.active_Persons)
p = Person("Joe","Smith",68)
p2 = Person("Lara", "Larrson", 27)
# print(Person.active_Persons)
# print(p2.log_out())
# print(Person.active_Persons)

