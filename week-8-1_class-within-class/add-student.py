class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name
class StudentClass():
    def __init__(self):
        self.__student_list = []
        # array
        # __student is private
    def add_student(self, student: Student):
        self.__student_list.append(student)
math_101 = StudentClass()
physic_101 = StudentClass()

s1 = Student(1, "Mary")
s2 = Student(2, "Bob")
math_101.add_student(s1)
math_101.add_student(s2)
physic_101.add_student(s2)