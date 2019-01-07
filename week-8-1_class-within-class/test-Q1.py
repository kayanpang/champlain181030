# testing Q1 in for loop
import random
number = random.randint(1,100)
For x in range (6)
    choice = input ("Please enter a number")
    if choice == number:
        print("you won.")
        break
    if x == 5:
        print("you lost")
        break
    if choice > number:
        print("you guessed too high")
    if choice < number:
        print("you guessed too low")