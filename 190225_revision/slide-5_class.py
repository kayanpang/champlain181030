# class is a blueprint or a set of instructions to build a specific type of objects
# an object or an instance is a specific object built from a specific class

# to define a method or function in a class
class Student:
    name = ""
    def myfunction(self):
        print(self.name)
# __init__ (initialize sets of each object at instantiation time
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)