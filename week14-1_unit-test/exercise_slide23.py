import re

# match: jim
# not match: jam, lam, 0am

# is_a_match = re.search("^jim$", "jim")
# is_a_match2 = re.search("^jim$", "j0m")

# want it to stop, so a dummy (a = 2) is put here
#a = 2

if re.search("^jim$", "jim"):
    print("This is a match")
else:
    print("Not a match")