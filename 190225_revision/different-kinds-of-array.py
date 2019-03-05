# list is ordered and changeable. Allows duplicate members. it uses [] square brackets
# – Use lists if you have a collection of data that does not need random access.
# Try to choose lists when you need a simple, iterable collection that is modified frequently.
mylist = [1, 2, 'Brendan']
print(mylist[1])

# tuple is ordered and unchangeable. Allows duplicate members. it uses () round brackets
# – Use tuples when your data cannot change.
mytuple = ('apple', 'banana', 'cherry', 1)
print(mytuple[1])


# a set is unordered and unindexed. it uses {} curly bracket
# need a for loop to get access to the set, cannot refer to index
# – Use a set if you need uniqueness for the elements
myset = {'apple', 'banana', 'cherry', 1, 2}
for x in myset:
    print(x)

# a dictionary is unordered, changeable and indexed. it has keys and values. it uses {} curly bracket
# can access the items in a dictionary using its key name
# When to use a dictionary:
# – When you need a logical association between a key:value pair.
# – When you need fast lookup for your data, based on a custom key.
# – When your data is being constantly modified. Remember, dictionaries are mutable.
# https://monjurulhabib.wordpress.com/2016/09/22/python-when-to-use-list-vs-tuple-vs-dictionary-vs-set-theory/
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