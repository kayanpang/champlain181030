import os

# my try
# try:
#    os.remove("d")
#    if IOError:
#        return os.mkdir("d")
# why return doesn't work: possible explanation
# That’s exactly what return is supposed to do. If at some point in a method you say return,
# it’s like saying "stop whatever it is you’re doing and get outta here NOW",
# so anything after the return keyword is ignored.
# https://www.codecademy.com/en/forum_questions/51c0e35d7c82caace80008b1

dirname = "TestDir"
# create function
def  create_dir_if_not_exist(name):
    if not os.path.isdir(name):
        os.mkdir(name)
        print("Directory" + name + " is created.")
    else:
        print("The supplied already exists.")