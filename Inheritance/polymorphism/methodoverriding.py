#method overriding : when mwthods having same name and same parameter in different class having parent and child relation between them
class parent:
    def properties(self):
        print("cash","Gold")
    def bike(self):
        print("Splender")
class Child:
    def bike(self):
        print("HB")
s = Child()
s.bike()