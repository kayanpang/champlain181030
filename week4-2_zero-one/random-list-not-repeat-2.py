import random
my_list = []

for x in range(20):

    rand_val = random.randint(1,100)
    for y in my_list:
        if y in my_list:
            if rand_val == y:
                continue
    my_list.append(rand_val)
# check out while loop as Carla suggested
