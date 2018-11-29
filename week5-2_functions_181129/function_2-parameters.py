# define a function with 2 parameters
def add_numbers(number1, number2):
    print(int(number1) + int(number2))

print("adding 1 + 2 gives")
# below is to define the parameters
add_numbers(1, 2)
# what if you don't give enough define, it will tell you missing positional argument
add_numbers(1)
# what if you give more parameter then set (it will  2 positional argument but 3 is given
add_numbers(1, 2, 3)