for a in range(1,26):

    if a % 3 == 0:
        print(str(a) + " fizz", end=" ")
    if a % 5 == 0:
        print(str(a) + " buzz", end=" ")
    if a % 3 == 0 and a % 5 == 0:
        print(str(a) + " fizzbuzz", end=" ")
    print(str(a))
