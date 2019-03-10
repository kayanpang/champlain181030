from math import pi

class Shape:
    def __init__(self, color):
    self._color = color

class Rectangle(Shape):
    def __init__(self, color, height, width):
        self.height = height
        self.width = width
        super().__init__(color)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.len + self.height)

class Square(Shape):
    len = 0
    def __init__(self, width):
        super().__init__(color, width, width)

    def get_width(self):
        return self.width

    def get_area(self):
        return self.len ** 2

    def get_perimeter(self):
        return self.len*4

class Circle(Shape):
    def __init__(self, color, radius):
        self.radius = radius
        super().__init__(color)

    def get_area(self):
        return pi * (self.__radius ** 2)

    def get_circumference(self):
        return 2 * pi * self.__radius

class Shapes:
    shape_list = []

    def add_shapes(self, shape: Shape):
        self.shape_list.append(shape)

    def delete_shapes(self, shape: Shape):
        self.shape_list.remove(shape)

    def clear_shapes(self):
        self.shape_list.clear()

    def get_total_area(self):
        total_area = 0
        for shape in self.shape_list:
            total_area += shape.get_area()
        return total_area

    def get_total_perimeter(self):
        total_perimeter = 0
        for shape in self.shape_list:
            total_perimeter += shape.get_perimeter()
        return total_perimeter

    def get_shape_count(self):
        count = len(shape_list)
            return count