from abc import ABC ,abstractmethod
class rcpit(ABC):
    @abstractmethod
    def student_details(self):
        pass
    @abstractmethod
    def student_assignment(self):
        pass
    @abstractmethod
    def student_marks(self):
        pass
class Copm_A(rcpit):
    def student_details(self):
        return "it will try to return the student details of computer A"
    def student_assignment(self):
        return "it will return student assignment of A"
    def student_marks(self):
        return "it will return student marks of A"
ca = Copm_A()
print(ca.student_assignment)
print(ca.student_details)
print(ca.student_marks)