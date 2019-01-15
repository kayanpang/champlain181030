import os

mylist = os.listdir()

for file_or_dir in mylist:
    if (os.path.isdir(file_or_dir)):
        print("Folder:")
    if (os.path.isfile(file_or_dir)):
        print("File :", end="")
    print(" " + file_or_dir)