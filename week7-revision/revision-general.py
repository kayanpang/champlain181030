# revision general list
magicians = ["alice", "david", "carol"]
for magician in magicians:
    print(magician)
# method .title
magicians = ["alice", "david", "carol"]
for magician in magicians:
    print(magician.title() + " , that was great!")
# create your own for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.title() + " are the fruits commonly seen in market.")

# testing sum
value_num = [1, 2, 3]
v_s = sum(value_num)
print(v_s)