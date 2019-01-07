class Person:
    def __init__(self):
        self.b = 1
# self.b is a public, it can be changed
class Student (Person):
    def __init__(self):
        self.b = 2
class GradStudent(Student):
    def __init__(self):
        self.b = 3

grad_student_1 = GradStudent()

grad_student_1.b = 6
grad_student_1.b = 71
grad_student_1.b = 72