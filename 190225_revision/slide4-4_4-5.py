# calling a function by using its name, with empty bracket()
def my_function():
    print("Hello from a function")
my_function()

# passing parameters to a function, order matters in the positioning of arguments
def full_name(fname, lname):
    print("Hello from a function " + fname + " " + lname)
full_name("Marie", "Curie")

# default value
def full_name_unknown(fname = "Unknown"):
    print("Hello" + fname)
full_name_unknown("Joe")
full_name_unknown()