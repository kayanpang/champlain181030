# slide 1-24, when an error is handled, it's referred to as an exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

# slide 1-25, try - except - else
first_number = input("please enter your 1st number")
second_number = input("please enter your 2nd number")
try:
    answer = int(first_number)/int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0")
print(answer)