# list is ordered and changeable. Allows duplicate members. it uses [] square brackets
mylist = [1, 2, 'Brendan']
print(mylist[1])

# tuple is ordered and unchangeable. Allows duplicate members. it uses () round brackets
mytuple = ('apple', 'banana', 'cherry', 1)
print(mytuple[1])


# a set is unordered and unindexed. it uses {} curly bracket
# need a for loop to get access to the set, cannot refer to index
myset = {'apple', 'banana', 'cherry', 1, 2}
for x in myset:
    print(x)

# a dictionary is unordered, changeable and indexed. it has keys and values. it uses {} curly bracket
# can access the items in a dictionary using its key name
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
y = mydict["model"]
print(y)
# use for loop to access to a dictionary
for key, value in mydict.items():
    print("\nKey: " + key)
    print("Value: " + value)