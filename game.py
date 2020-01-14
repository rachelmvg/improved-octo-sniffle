# This is going to be a game!
# It will a number guessing game: the computer will pick a number
# And the human will have to guess what number it is.

# First, we need to import the random package and generate a number
import random

MAX_NUMBER = 20

number = random.randint(1, MAX_NUMBER)

# Ask the user for their first guess
userGuess = int(input('What do you think, the number is?'))

print(f'You guessed:{userGuess}')
if userGuess == number:
    print('That is correct!')
else:
    difference = abs(userGuess - number)
    if difference > 10:
        specification = 'waaaay too'
    if difference > 5:
        specification = 'too'
    else:
        specification = 'a bit too'
    
    if userGuess > number:
        print(f'That is {specification} large!')
    else:
        print(f'That is {specification} small!')

print(number)