import os
# mylist = os.listdir()
# print(mylist)
# it will print ['directory_exercise1.py', 'exercise_display-files.py', 'os.py', 'personal_code', 'school_code']

# teacher's starter's structure
# while True:
#    listing = os.listdir()
#    print("-"*50)
#    for file in listing:
#        print(file)
#    print("-"*50)
#    a = input("Selection? >")



while True:
    mylist = os.listdir()
    print("-" * 50)
    for file_or_dir in mylist:
        if (os.path.isdir(file_or_dir)):
        print("Folder:")
        print(" " + file_or_dir)

    print("-" * 50)
    print(" " + file_or_dir)