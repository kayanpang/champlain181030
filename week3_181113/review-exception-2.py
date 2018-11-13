x = input('Enter the age you started to work >')
y = input('Enter your current age >')
try:
    z = int(y) - int(x)
except ValueError:
    print("The value(s) entered is not numeric")
print('You have been working for {0} years'.format(z))