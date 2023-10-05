from abc import ABC,abstractmethod
class Course(ABC):
    def __init__(self,title,duration,price):
        self.title =title
        self.duration = duration
        self.price =price
    def enroll(self):
        pass
    @abstractmethod
    def get_details(self):
        pass

class ProgrammingCourse(Course):
    def __init__(self,Programming_language,instructor):
        self.Programming_language =Programming_language
        self.instructor = instructor
        pass
