# break
for b in range(10):
    if b == 3:
        break
    print(b)

# continue
for c in range(10):
    if c == 3:
        continue
    print(c)

# break in slide 1-30
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        break
    print('Number is ' + str(number))
print("out of loop")