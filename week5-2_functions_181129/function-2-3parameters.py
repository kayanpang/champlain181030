def add_3_numbers(number1, number2, number3):
    print("adding 3 numbers")
    print(int(number1) + int(number2) + int(number2))

def add_numbers(number1, number2, number3):
    print("adding 2 numbers")
    print(int(number1) + int(number2))

# you can only have one name for one function

print("adding 1 + 2 gives")
add_numbers(1, 2)

print("adding 1 + 2 + 3 gives")
add_3_numbers(1, 2, 3)

# control + slash will make the text as comment
# def add_numbers(number1, number2, number3):
#     print("adding 2 numbers")
#     print(int(number1) + int(number2))