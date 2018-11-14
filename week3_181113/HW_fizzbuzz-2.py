for a in range(26):
    if a % 3 == 0:
        if a % 5 == 0:
            print(str(a) + "fizzbuzz")
        else:
            print(str(a) + "buzz")
    elif a % 5 == 0:
        print(str(a) + "fizzbuzz")
    else:
        print(str(a))