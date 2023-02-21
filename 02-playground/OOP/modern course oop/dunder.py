class A:
    def __init__(self,name,last):
        self.name = name
        self.last = last

    def __add__(self,other):
        return f"{self.name} {other.last}"

j = A("mina",'aziz')
k = A('hala', 'william')

print(j+k)