class Person:
    active_persons = 0 

    @classmethod
    def display_active_persons(cls):
        return f'there are {cls.active_persons} active persons now.'
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        Person.active_persons += 1
    
    def logout(self):
        Person.active_persons -= 1
        return f"{self.first} has logged out\n{Person.active_persons} active now."
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

p1 = Person('mena','aziz',16)
p2 = Person('hania','kamel', 21)

print(p2.initials())
print(Person.display_active_persons())
print(p1.logout())