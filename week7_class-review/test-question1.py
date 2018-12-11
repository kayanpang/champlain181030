# number guessing
import random
my_list = []
for x in range(1):
    my_list.append(random.randint(1,100))
n = input("Please guess a number between 1 and 100")

if n > x:
    print("Wrong guess, you guessed too high.")
    elif n == x:
    print("Correct! You Win!")
    else:
    print("Wrong guess, you guessed too low.")

guess = 0
While true:

    for guess in range(6)
        if guess == 6:
            print("Sorry, you didn't guess the correct number. the correct number was " + str(x))