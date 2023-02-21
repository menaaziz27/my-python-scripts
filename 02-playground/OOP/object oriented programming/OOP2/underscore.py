#_name   >>> if you want to tell that it's a private item
#__name  >>> specific to single class
#__name__  >>> magic methods

class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.__msg = "HAHAHAHA"

user = Person("peir" , "smith")

print(user)
print(user.first)
print(user.last)
print(dir(user))
print(user._Person__msg)
