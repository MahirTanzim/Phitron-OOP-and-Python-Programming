class StudentDatabase:
    student_list = []           #Task 1

    @classmethod
    def add_student(cls, student):              
        cls.student_list.append(student)


class Student:          #Task 2
    def __init__(self, student_id, name, department, is_enrolled=False):
        self._student_id = student_id       #Task 9 Protected attribute
        self._name = name                   #Task 9 Protected attribute
        self._department = department       #Task 9 Protected attribute
        self._is_enrolled = is_enrolled     #Task 9 Protected attribute
        StudentDatabase.add_student(self)       #Task 3

    def enroll_student(self):           #Task 4
        if self._is_enrolled:
            print(f"Student {self._student_id} Name: {self._name} is already enrolled.")        #Task 8 Error Handling
        else:
            self._is_enrolled = True
            print(f"Student {self._student_id} Name: {self._name} has been enrolled.")

    def drop_student(self):         #Task 5
        if not self._is_enrolled:
            print(f"Student {self._student_id} Name: {self._name} is already not enrolled.")        #Task 8 Error Handling
        else:
            self._is_enrolled = False
            print(f"Student {self._student_id} Name: {self._name} has been dropped.")

    def view_student_info(self):        #Task 6
        print("| {:<10} | {:<20} | {:<20} | {:<12} |".format(self._student_id, self._name, self._department, "Enrolled" if self._is_enrolled else "Not Enrolled"))
        print("-" * 75)


def find_student(student_id):
    for student in StudentDatabase.student_list:
        if student._student_id == student_id:
            return student
    return None


def menu():             #Task 7
    while True:
        print("\n    Student Management System ")
        print("-------------------------------------")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            if not StudentDatabase.student_list:
                print("No students found in the DataBase.")
            else:
                print("-" * 75)
                print("| {:<10} | {:<20} | {:<20} | {:<12} |".format("ID", "Name", "Department", "Status"))
                print("-" * 75)
                for student in StudentDatabase.student_list:
                    student.view_student_info()

        elif choice == '2':
            student_id = input("Enter Student ID to enroll: ")
            student = find_student(student_id)
            if student:
                student.enroll_student()
            else:
                print("Error: Student ID not found.")

        elif choice == '3':
            student_id = input("Enter Student ID to drop: ")
            student = find_student(student_id)
            if student:
                student.drop_student()
            else:
                print("Error: Student ID not found.")

        elif choice == '4':
            print("Exiting the system....")
            break
        else:
            print("Invalid Key. Please try again.")




Student("101", "Mahir Tanzim", "CSE", False)
Student("102", "Rifat Kabir", "EEE", False)
Student("103", "Badhon Ahmed", "Textile", True)
Student("104", "Mustazir Billah", "CSE", False)
Student("105", "Sabbir Ahmed", "EEE", True)

menu()
