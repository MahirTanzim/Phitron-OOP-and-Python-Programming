import random
from school import School
class Person:
    def __init__(self, name):
        self.name = name



class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)
    

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom  # classroom object
        self.__id = None
        self.marks = {}         # {"eng" : 90, "ICT" : 70}
        self.subject_grade = {} # {"Eng" : "A"}
        self.grade = None       # Final Grade

    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade=grade)
            sum+=point

        if len(self.subject_grade) == 0:
            gpa = 0.00
            return f"{self.name} Final Grade : F with GPA : {gpa}"
        else:
            gpa = sum / len(self.subject_grade)
            self.grade = School.value_to_grade(value=gpa)
            return f"{self.name} Final Grade : {self.grade} with GPA : {gpa}"

    @property
    def id (self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

