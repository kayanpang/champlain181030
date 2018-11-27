# case 1
counter = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            counter = counter + 1
# this will execute 8 times
print("the number of times this looped is " + str(counter))

# case 2
counter = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x,y,z)
# this will execute 8 times
# print(x,y,z) will print what is the state
print("the number of times this looped is " + str(counter))

# case 3
counter = 0
for x in range(2):
    print(x, end="")
    for y in range(2):
        for z in range(2):
            print(x,y,z)
# this will execute 8 times
# print(x,y,z) will print what is the state
print("the number of times this looped is " + str(counter))

# case 3 abcdef
for x in ["a", "b"]:
    for y in ["c", "d"]:
        for z in ["e", "f"]:
            print(x,y,z)