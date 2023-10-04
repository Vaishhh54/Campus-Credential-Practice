class Person:
    def fun(self,name,age):
        self.name = ""
        self.age = 0
    
class Student(Person):
    def info(self):
        self.student_id = input("Enetr studnet id")
    def display(self):
        print("Student id : ",self.student_id)
        print("student_name: ",s.name)
        print("student age ",s.age)
name = input("Enter Name")
age = int(input("Enter age: "))
s= Student()
s.info()
s.display()
    