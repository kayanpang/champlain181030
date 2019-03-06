import re
Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]
characters = []

# for i in Input_list:
#     if not isinstance(i, int):
#         characters.append(i)
# else:
#     pass
#
# print(characters)

for i in Input_list:
    if i.isalpha():
        characters.append(i)
    else:
        pass

print(characters)