class A:
    def demo(self):
        self.gold
        self.cash
    def properties(self):
        print("This is parents class method")
class B:
    def  show(self):
        print("This is child class method")
class C:
    def show(self):
        print("class C")
class D(A,B,C):
    def show():
        print("This is Class D")
s1 = A()
s2 = B()
s3 = C()
s4 = D()
s4.properties()
