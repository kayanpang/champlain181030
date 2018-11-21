import random
list = []
# create an empty list
for a in range(11):
# for X in range (#) the command will be repeated for # times
   list.append(random.randint(1, 100))
   print(list[a])
a = (len(list))
print(a)
