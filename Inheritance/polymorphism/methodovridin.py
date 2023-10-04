class A:
    def show(self):
        print("class A")  #
class B:
    def show(self):
        print("class B")
class C(A,B):
    def showC(self):
        print("class C")

s = C()
s.show()