filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # readlines()method takes each line from the file and stores it in a list
for line in lines:
    print(line.rstrip())