def is_num_negative(n):
    if n < 0:
        return True
    return False

the_number = input("enter a number")

if is_num_negative(int(the_number)):
    print("negative")
else:
    print("positive")