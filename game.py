# This is going to be a game!
# It will a number guessing game: the computer will pick a number
# And the human will have to guess what number it is.

computersNumber = 7

userGuess = input('What do you think, the number is?')

print(f'You guessed:{userGuess}')
if int(userGuess) == computersNumber:
    print(f'That is correct!')
else:
    print('That is wrong!')        