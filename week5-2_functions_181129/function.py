# example: repetition
print("this is line 1")
print("---------------")
print("this is line 2")
print("---------------")
print("this is line 3")
print("---------------")
# so create a function to do this repetition
def print_underscores():
    print("---------------")
# function needs to be defined before used
print("this is line 1")
print_underscores()
print("this is line 2")
print_underscores()
print("this is line 3")
# give a line to separate between function line
def print_equal():
    print("==========")

def print_dash():
    print("___---___")

def print_separator(width):
    for w in range(width):
        print("*", end="")

print("this is line 1")

print_separator(50)