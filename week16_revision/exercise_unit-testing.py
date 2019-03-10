import unittest
from math import pi
from .exercise_object-oriented import *

class Testing(unittest.TestCase):
    shapes = Shapes()

    def test_rectangle(self):
        rectangle = Rectangle("Red", 2, 3)
        area = rectangle.get_area()
        self.assertEqual(area, 6)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle("Red", 2, 3)
        perimeter = rectangle.get_perimeter()
        self.assertEqual(perimeter, 10)

    def test_square(self):
        square = Square("Red", 3)
        area = square.get_area()
        self.assertEqual(area, 9)

    def test_square_perimeter(self):
        square = Square("Red", 3)
        perimeter = square.get_perimeter()
        self.assertEqual(perimeter, 12)

    def test_circle(self):
        circle = Circle("Red", 3)
        area = circle.get_area()
        expected_area = pi * (3 * 2)
        self.assertEqual(area, expected_area)

    def test_circumference(self):
        circle = Circle("Red", 3)
        circumference = circle.get_circumference()
        expected_circumference = 2 * pi * 3
        self.assertEqual(circumference, expected_circumference)

    def test_shapes_add(self):
        circle = Circle("Red", 3)
        self.shapes.add(circle)
        square = Square("Red", 3)
        self.shapes.add(square)
        rectangle = Rectangle("Red", 2, 3)
        self.shapes.add(rectangle)
        expected_area = rectangle.get_area()+square.get_area()+circle.get_area()
        total_area = self.shapes.get_total_area()
        self.assertEqual(total_area, expected_area)

    def test_shapes_clear(self):
        self.shapes.clear()
        total_area = self.shapes.get_total_area()
        expected_area = 0
        self.assertEqual(total_area, expected_area)