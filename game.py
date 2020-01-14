# This is going to be a game!
# It will a number guessing game: the computer will pick a number
# And the human will have to guess what number it is.

# First, we need to import the random package and generate a number
import random

MAX_NUMBER = 5

number = random.randint(1, MAX_NUMBER)

# Ask the user for their first guess
correctGuess = False

while not correctGuess:
    userGuess = int(input('What do you think, the number is?'))
    correctGuess = userGuess == number
    
    print(f'You guessed:{userGuess}')
    if userGuess == number:
        print('That is correct!')
    elif userGuess > number:
        print('That is waaay too large!')
    else:
        print('Think bigger')

print(number)