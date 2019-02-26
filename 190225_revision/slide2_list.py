# to access a member of the list, use the indexer

alist = [1, 2, "Brendan"]
print(alist[1])
print(alist)
alist.append('another value')
print(alist)
alist.remove('another value')
print(alist)
alist2 = alist +[4,5,6]
print(alist2)

mylist = [1, 3, 5, 6, 8, 10]
print(mylist[0:6])