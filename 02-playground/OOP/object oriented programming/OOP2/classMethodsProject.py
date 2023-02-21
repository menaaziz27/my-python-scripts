with open('csv.txt' , 'w') as f:
    f.write('mena,aziz,18\n')
    f.write('maged,kamel,20\n')
    f.write('soha,mobarak,62\n')
    f.write('joy,ashraf,22\n')

class Person:
    def __init__(self,first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.display()
    @classmethod
    def instances(cls, str_data):
        first,last,age = str_data.split(',')
        return cls(first,last,int(age))

    def display(self):
        print(f"{self.first} {self.last} {self.age}")
        
with open('csv.txt') as file:
    for line in file:
        if not line.isspace():
            Person.instances(line)