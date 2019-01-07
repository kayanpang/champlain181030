class Student():
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa


class StudentClass():
    def __init__(self):
        self.__student_list = []

# array
# __student is private

    def add_student(self, student: Student):
        self.__student_list.append(student)

    def remove_student(self, student_id):
        for current_student in self.__student_list:
            if current_student.id == student_id:
                self.__student_list.remove(current_student)
    def list_students(self):
        for student in self.__student_list:
            print ("Student ID " + str(student.id) + " Student Name " + student.name)
    def get_count_of_students(self):
        return len(self.__student_list)
    def get_average_gpa(self):
        gpa_sum = 0
        for student in self.__student_list:
            sum(self.gpa)
        return gpa_sum/len(self.__student_list)


math_101 = StudentClass()

s1 = Student(100, "Mary", 3.5)
s2 = Student(200, "Bob", 2.8)
s3 = Student(300, "Brendon", 3.2)
math_101.add_student(s1)
math_101.add_student(s2)
math_101.add_student(s3)
math_101.remove_student(200)

# i = 9
# this is here to test code
math_101.list_students()
#ask it to show the list
math_101.get_average_gpa()