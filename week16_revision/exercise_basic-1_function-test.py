Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]

def is_number(s):
    if isinstance(s, int):
        return True
    return False

def is_even(s):
    if s % 2 == 0:
        return True
    return False

def max():
    max_value = 0
    for item in Input_list:
        if is_number(item):
            if int(item) > max_value:
                max_value = item
    return max_value

def is_alpha(s):
    if isinstance(s, int):
        pass
    elif s.isalpha():
        return True
    return False


counter = 0
for item in Input_list:
    if is_number(item):
        print("Element # " + str(counter) + " " + str(item))
        if is_even(item):
            print("This is an even number")
        else:
            print("This is an odd number")
        if item < max():
            print(str(item) + " is not the highest number")
        else:
            print(str(item) + " is the highest number")
    counter += 1

for character in Input_list:
    i = []
    if is_alpha(character):
        i.append(character)
print("the character found are " + sorted.i)