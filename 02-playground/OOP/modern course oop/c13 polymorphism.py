#example of polymorphism
#one method is implemented in both the subclass and the parent class but do different things
class Animal:
    def speak(self):
        raise NotImplementedError("This method should be implemented in subclass")
class Cat(Animal):
    def speak(self):
        print("meow")    
class Dog(Animal):
    def speak(self):
        print("woof")    

d = Dog()
d.speak()
a = Animal()
a.speak()