class Employee:
    def __init__(self,name,empid,salary):
        self.name =""
        self.empid = ""
        self.salary =0.0
    def work(self):
        print("Working on java Devlopment")
    def setSalary(self,salary):
        self.salary = salary
        
    def getSalary(self):
        return self.salary

class hrManager(Employee): 
    def __init__(self,name,empid,salary,dep):
        super.__init__(name,empid,salary)
        self.dep = dep
    
    def work(self):
        print("working on making coffe for HR")
    
    def addEmployee(self):
        self.name = input("Enter name: ")
        self.empid = input("Enter Emloyee id: ")
        self.salary = int(input("Enter Employee salary"))
        super().setSalary()
        self.dep = input("Enter Department")

        self.dep = input("Enter Department")
emp1 = Employee()
emp2 = hrManager()
emp1.addEmployee()


    
