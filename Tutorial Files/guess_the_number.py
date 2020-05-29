# This is a guess the number game.

import random
secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range (1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Too low!')
    elif guess > secret_number:
        print('Too high!')
    else:
        break   # This condition is the correct guess.

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('That is incorrect. The number I had in mind was ' + str(secret_number) + '.')
