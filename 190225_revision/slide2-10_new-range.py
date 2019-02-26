# combining for and range to make a new range
squares = [value**2 for value in range(1,11)]
print(squares)

# to create a list with range, create a range from 2 to 10, skip every 2
even_numbers = list(range(2,11,2))
print(even_numbers)

# crash course ch4, p.63
squares2 = []
for value in range(1,11):
    squares2.append(value**2)
print(squares2)