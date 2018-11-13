x = input ("enter a number:")
y = input ("enter another number:")

try:
    result = (int(x)/int(y))
except ZeroDivisionError:
    print("you can't divide by zero!")
