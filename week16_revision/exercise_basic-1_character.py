Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]
characters = []

def alpha(self):
    return [i for i in Input_list if i.isalpha()]
print(alpha(Input_list))
