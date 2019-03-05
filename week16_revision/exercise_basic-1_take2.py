Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]
numbers = []

for i in Input_list:
    if isinstance(i, int):
        numbers.append(i)
    else:
        pass
print(numbers)