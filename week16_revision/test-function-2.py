shape_list = []


def add_shape(shape="square"):
    shape_list.append(shape)

def get_shape_count():
    count = len(shape_list)
    return count

add_shape("circle")
add_shape("triangle")
add_shape("square")
print(shape_list)