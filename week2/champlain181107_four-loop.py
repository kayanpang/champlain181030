for t in range(10):
    print(t)
    print(t+1)

print("Program run has ended")

for t in range(4):
    print(t+1)
    print('*', end="")
print("Program run has ended")

for y in range(0,4):
    print(str(y) + ":", end="")
    for x in range(y):
        print('*', end="")
print()