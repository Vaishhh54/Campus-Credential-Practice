class parent1:
    def show1(self):
        print("Parent method")
class chlid(parent1):
    def show2(self):
        super().show1()
        print("child classs")
s = chlid()
s.show2()
