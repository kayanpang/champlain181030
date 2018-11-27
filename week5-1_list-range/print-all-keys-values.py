countries = {'us': 'USA','fr': 'France','uk': 'United Kingdom'}

for k, v in countries.items():
    print(k,v)
print ("-----------------")
# if I just want to print the value
for i in countries.items():
    print(i[1])
print ("-----------------")
for a,b in countries.items():
    print(b)

print("-----------------")

for a in countries.keys():
    print(a)

print("-----------------")

for v in countries.values():
    print(v)