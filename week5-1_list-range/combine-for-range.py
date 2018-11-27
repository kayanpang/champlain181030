# hard coding list first
my_list = [11, 22, 33, 44]

for item in my_list:
    print(item)
# ------------------------------
squares = [value**2 for value in range(1,11)]
# take a value between 1-11, then square it
print(squares)

# try to formulate a list [11, 22, 33, 44]
my_list_2 = [value*11 for value in range(1, 5)]
print(my_list_2)

# first 10 values of 2**n
my_list_3 = [2 ** n for n in range(11)]
print(my_list_3)