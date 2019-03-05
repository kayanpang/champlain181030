Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]

highest_number = max([i for i in Input_list if isinstance(i, int)])
print(highest_number)
