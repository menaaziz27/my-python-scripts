class User:
    Active_Users = 0
    @classmethod
    def display_active_users(cls):
        return f"active users are {cls.Active_Users} now."
    
    @classmethod
    def from_string(cls, new_string):
        first,last,age = new_string.split()
        return cls(first, last, int(age))
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.Active_Users += 1

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def fullname(self):
        return f"{self.first} {self.last}"

class Moderator(User):
    active_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.active_mods += 1

u1 = User('mena', 'aziz' , 21)
u2 = User('rola', 'aziz' , 22)
u3 = User('kero', 'aziz' , 28)
print(User.Active_Users)
m1 = Moderator('hala', 'aziz' , 55, "piano")
m2 = Moderator('aziz', 'kamel' , 59, "car")
print(User.Active_Users)
print(Moderator.active_mods)
