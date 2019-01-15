import os

mylist = os.listdir()
a += 1
for file_or_dir in mylist:
    if (os.path.isdir(file_or_dir)):
        print("Folder:" + str(a + 1))
        print(" " + file_or_dir)