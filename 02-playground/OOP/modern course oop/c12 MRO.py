class A:
    # pass
    def do_something(self):
        print("method defined in : A")
class B(A):
    pass
    # def do_something(self):
    #     print("method defined in : B")
    #     super().do_something()
class C(A):
    pass
    # def do_something(self):
    #     print("method defined in : C")
class D(B,C):
    pass
    # def do_something(self):
    #     print("method defined in : D")                

D = D()
D.do_something()