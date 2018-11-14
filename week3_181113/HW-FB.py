for a in range(1,25):

    if a % 3 == 0:
        print("fizz", end=" ")
    if a % 5 == 0:
        print("buzz", end=" ")
    if a % 3 == 0 and a % 5 == 0:
        print("fizzbuzz", end=" ")
    print(str(a))
