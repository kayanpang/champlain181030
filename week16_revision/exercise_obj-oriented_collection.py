from .exercise_object-oriented import Shape

shape_list = []
area_list = []
perimeter_list = []



class Collection:
    def add_shape(shape = "square"):
        shape_list.append(shape)

    def delete_shape(shape = "square"):
        shape_list.remove(shape)

    def clear_shape(self):
        shape_list.clear()

    def add_shape_area(area = 0):
        area_list.append(area)

    def add_perimeter(perimeter = 0):
        perimeter_list.append(perimeter)

    def get_shape_count(self):
        count = len(shape_list)
        return count

    def get_total_area(self):
        total_area = sum(area_list)
        return total_area

    def get_total_perimeter(self):
        total_perimeter = sum(perimeter_list)
        return total_perimeter
