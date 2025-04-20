class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self)  -> str:
        return f"Student: {self.name}, Class: {self.current_class}, ID: {self.id}"

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__ (self) -> str:
        return f"Teacher: {self.name}, Subject: {self.subject}, ID: {self.id}"

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, cls,  fee):
        if fee < 6000:
            return "Not enough fee"
        else:
            id = len(self.students) + 1
            student  = Student(name, cls, id)
            self.students.append(student)
            return f"{name} is enrolled in class {cls} with ID: {id}"

    def __repr__(self):
        print(f"Welcome to {self.name}")
        print("------Our Teacher------")
        for teacher in self.teachers:
            print (teacher)
        print("------Our Students------")
        for student in self.students:
            print(student)
        return ""
    


phitron = School("Phitron")

phitron.enroll('Mahir', 4, 7000)
phitron.enroll("Maisha", 4, 5000)
phitron.enroll("Jony", 4, 70007)
phitron.enroll("Roni", 4, 12345)


phitron.add_teacher("Tom Cruz", "Algorithm")
phitron.add_teacher("Decap", "DS")
phitron.add_teacher("Aj", "DBMS")


print(phitron.students[0].name)
