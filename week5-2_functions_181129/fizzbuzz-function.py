def is_divisible(num, test_num):
    if num % test_num == 0:
        return True
    return False

for num in range(0, 26):
    print(str(num) + ":", end="")
    if is_divisible(num, 3) and is_divisible(num, 5):
        print("FizzBuzz")
    elif is_divisible(num, 3):
        print("Fizz")
    elif is_divisible(num, 5):
        print("Buzz")
    else:
        print()
# the code is as long, but more manageable (you just have to change one thing)
# read python crash course chapter 8 functions
# study chapter 9 classes (pt to pt...)
