class A:
    def __init__(self):
        self.gold
        self.cash
    def properties(self):
        print("This is parents class method")
class B(A):
    def  showB(self):
        print("This is child class method")
class c(B):
    def show(self):
        print("class C")

obj1 = A()
obj2 = B()
obj3 = C()
