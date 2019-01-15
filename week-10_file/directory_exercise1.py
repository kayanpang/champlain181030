import os

# my try
# try:
#    os.remove("d")
#    if IOError:
#        return os.mkdir("d")

dirname = "TestDir"
# create function
def  create_dir_if_not_exist(name):
    if not os.path.isdir(name):
        os.mkdir(name)
        print("Directory" + name + " is created.")
    else:
        print("The supplied already exists.")