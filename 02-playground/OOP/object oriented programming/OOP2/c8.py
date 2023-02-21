#inheritance 
#isinstance() method

class Animal:
    cool = True

    def some_sound(self, sound):
        return f"it says {sound}"

class Cat(Animal):
    pass

lion = Animal()
cat = Cat()
print(lion.some_sound("ROOOOAR"))
print(cat.some_sound("meow"))

print(isinstance(lion, Animal))