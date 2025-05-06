from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

# adding classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


# adding student
rahim = Student("Rahim", eight)
Fahim = Student("Fahim", nine)
Rakib = Student("Rakib", eight)
Hamim = Student("Hamim", ten)


school.student_admission(rahim)
school.student_admission(Fahim)
school.student_admission(Rakib)
school.student_admission(Hamim)

# adding teacher

abul = Teacher("Abul Khan")
Babul = Teacher("Babul Khan")
Kabul = Teacher("Kabul Khan")


# adding subject

bangla = Subject("Bangla", abul)
Physics = Subject("Physics", Babul)
Chemistry = Subject("Chemistry", Kabul)
Math = Subject("Math", Babul)


eight.add_subject(bangla)
eight.add_subject(Physics)
eight.add_subject(Math)
nine.add_subject(Physics)
nine.add_subject(Math)
ten.add_subject(Math)
ten.add_subject(Physics)
ten.add_subject(bangla)
ten.add_subject(Chemistry)



eight.take_semester_exam()
nine.take_semester_exam()
ten.take_semester_exam()
print(school)