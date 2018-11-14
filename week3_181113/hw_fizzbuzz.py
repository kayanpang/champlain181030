
for a in range(26):
    if a % 3 == 0 and a % 5 == 0:

            print(str(a) + "fizzbuzz")

    elif a % 3 == 0 and a % 5 != 0:
        print(str(a) + "fizz")
    elif a % 3 != 0 and a % 5 == 0:
        print(str(a) + "buzz")
    else:
        print(str(a))