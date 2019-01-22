# file open close with try/finally clause
try:
    f = open("text.txt", encoding = 'utf-8')
    print(f.read())
finally:
    f.close()

# file open close "with" statement, anything under with (the indentation)
with open("text.txt", encoding = 'utf-8') as text:
    content = text.read()
    print(content)

# read a bit of a file
f = open("text.txt", encoding = 'utf-8')
print(f.read(4))

# write/append
with open("file.txt", 'a') as file_object:
    file_object.write("Thanks!")

# r or rt = read
# w = write
# b = binary
# binary example = image, f = open("img.bmp",'r+b')