import random
list = []
# create an empty list
for a in range(10):
# for X in range (#) the command will be repeated for # times
   list.append(random.randint(1, 100))
   print(list[a])
maxVal = list[0]
for y in list:
   if y > maxVal:
       maxVal = y
print(maxVal)
minVal = list[0]
total = 0
cont = 0
for y in list:
    if y < minVal:
        minVal = y
    total = total + y
    cont += 1
av = total/10
print(minVal)
print(av)
print(cont)
