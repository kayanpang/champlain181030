class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Students():
    def __init__(self):
        self.__student_list = []
    def add_student(self, student: Student):
        self.__student_list.append(student)
s1 = Student(1, "Mary")
s2 = Student(2, "Bob")
slist.add_student(s1)
slist.add_student(s2)