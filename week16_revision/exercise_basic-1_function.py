import string
Input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "P6"]
numbers = []
number_divisible = []
characters = []
punctuation = []

def punctuation(s):
    for i in string.punctuation:
        if s == i:
            return True
        return False

def isnumber(s):
    for i in s:
        if isinstance(i, int):
            return True
        return False
        if i % 2 == 0:
            return True
        return False
        elif i.isalpha():
        

