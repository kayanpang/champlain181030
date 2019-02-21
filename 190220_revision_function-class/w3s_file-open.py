# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)

# open and read file
f = open("demofile.txt", "r")
print(f.read())

# open and read part of the file
f = open("demofile.txt", "r")
print(f.read(5))

# open file and read line
f = open("demofile.txt", "r")
print(f.readline())

# open file and read the first 2 lines
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# use for loop for read the whole file line by line
f = open("demofile.txt", "r")
for x in f:
    print(x)