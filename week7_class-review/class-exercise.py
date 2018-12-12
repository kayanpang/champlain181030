# the goal is to get area
from math import pi
class Shape:
    color = ""

class Circle(Shape):
    radius = 0
    # constructor
    def __init__(self, c, r):
        self.radius = r
        self.color = c

    def get_area(self):
        return pi * (self.radius ** 2)

class Rectangle(Shape):
    len = 0
    height = 0
    # constructor
    def __init__(self, c, h, l):
        self.height = h
        self.len = l
        self.color = c

    def get_area(self):
        return self.len * self.height

my_shape = Rectangle("Red", 5, 10)
print(my_shape.get_area())
# would there be a difference if color is not in the contructor of the class Rectangle?