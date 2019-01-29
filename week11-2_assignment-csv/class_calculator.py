import random
class Calculator:

    def __init__(self, list=[]):
        self.__list = list

    def get_average (self):
        # to get average, sum (total) of the list / length of the list
        # not knowing how many numbers are in the list
        total = 0
        for item in self.__list:
            total += item
            # with += within a loop
            return total / len(self.__list)


    def get_max (self):
        # not knowing what are the number of the list
        max_val = self.__list[0]
        for item in self.__list:
            if item > max_val:
                max_val = item
        return max_val

    def get_min (self):
        # try to follow the example of get_max
        min_val = self.__list[0]
        for item in self.__list:
            if item < min_val:
                min_val = item
        return min_val

    def Clear_list (self):
        # to clear a list, use clear()
        self.__list.clear()
        print(self.__list)

    def generate_random_data (self, x, y, z):
        # review random data from min-max from week4-2
        # we don't know the amount of # we have in the list so put it as x
        # we don't know the list start and end, so put it as y and z
        r_list = []
        for w in range(x):
            r_list.append(random.randint(y,z))
        return r_list