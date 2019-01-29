f = open("test_file.txt", "w+")
f.write("Champlain VR")
# this is the line to insert
f.seek(0)
print(f.read())