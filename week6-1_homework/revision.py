# revision
message = "hello world"
# message is a variable, "hello world" is a value
print(message)

# string is anything with "", and those start with str
# list is a collection of item in a particular order in []
bicycles = ["trek", "cannondale", "redline"]
print(bicycles)

# list in for loop
magicians = ["alice", "bob", "Carol"]
for magician in magicians:
    print(magician)

# if statement setting up a condition: if it's the case, print/do, if not, do something else
cars = ["audi", "bmw", "subaru"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# dictionary is a collection of key-value pairs, use {}
alien = {"color": "green", "tentacle": 8}

# input and while loop (we can execute a statement as long as a condition is true
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
