# find min, max, length, sum, and average of a
# list of 10 random numbers.

import random

my_list = []
for x in range(10):
    my_list.append(random.randint(1,100))

max_of_the_list = my_list[0]
min_of_the_list = my_list[0]
sum_of_the_list = 0
length_of_the_list = 0

for x in my_list:
    # this statement will run 10 times
    length_of_the_list += 1
    sum_of_the_list += x
    # sum=sum+x
    if x > max_of_the_list:
        max_of_the_list = x
        # print("x= " + str(x))
        #print("Max = " + str(max_of_the_list)
    if x < min_of_the_list:
        min_of_the_list = x
print("sum = " + str(sum_of_the_list))
print("size = " + str(length_of_the_list))
print("largest = " + str(max_of_the_list))
print("smallest = " + str(min_of_the_list))

average_of_the_list = sum_of_the_list / length_of_the_list
print("Average = " + str(average_of_the_list))

# test (print) if you're not sure of your code

# what if you want to make sure there's no duplicate