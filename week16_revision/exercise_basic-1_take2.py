import string
Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]
numbers = []
number_divisible = []
characters = []
punctuation = []

for i in Input_list:
    if isinstance(i, int):
        numbers.append(i)

        if i % 2 == 0:
            number_divisible.append(i)
    elif i.isalpha():
            characters.append(i)


    else:
        pass

print(numbers)
print(number_divisible)
print(max(number_divisible))
print(sorted(characters))