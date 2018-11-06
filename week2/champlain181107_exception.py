x = input ("enter a number:")
y = input ("enter another number:")

try:
    result = (int(x)/int(y))
except ZeroDivisionError:
    print("you can't divide by 0!")
except ValueError:
    print("Please use value 0 - 9 (Except as a divisor!)")
except Exception:
    print("an unknown error has occured")
else:
    print(int(x)/int(y))