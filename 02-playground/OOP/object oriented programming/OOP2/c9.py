class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age > 0:
            self._age = age
        else:
            self.age = 0

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, new_name):
        self.first, self.last = new_name.split()

jane = Human('jane', 'goodall', 50)

print(jane.fullname)
jane.fullname ="Tim hamada"
print(jane.fullname)
