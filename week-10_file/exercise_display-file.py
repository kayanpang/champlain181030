# teacher's answer
import os

while True:
    listing = os.listdir()
    print("-" * 50)
    counter = 1

    for file in listing:
        print(counter, end="")
        if os.path.isdir(file):
            print("(folder)", end="")
        else:
            print("( file )", end="")
        print(file)
        counter += 1

    print("-"*50)

    a = input("Selection? >")
    myfile = listing[int(a) - 1]

    if os.path.isfile(myfile):
        with open(myfile, "r") as f1:
            print(f1.read())

    if os.path.isdir(myfile):
        os.chdir(myfile)

    if a == ".." or a == "back":
        os.chdir("..")
        print("Backed up one folder")