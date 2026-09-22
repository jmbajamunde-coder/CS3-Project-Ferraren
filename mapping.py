class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


course = Course("Computer Science")

student1 = Student("Giulia", "S001")
student2 = Student("Matt", "S002")
student3 = Student("Ashley", "S003")

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

print("Course:", course.name)
print("Students:")

for student in course.students:
    print(student.student_id, "-", student.name)
