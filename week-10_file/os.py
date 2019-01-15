import os
f2 = open("seektest.txt", "r")
print(f2.read())
f2.close()

os.remove("seektext.txt")

try:
    os.remove("seektext.txt")
except IOError:
    print("Caught an IO error")
except Exception:
