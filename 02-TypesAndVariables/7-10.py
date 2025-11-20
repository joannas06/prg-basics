###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
print('The computer is playing now!')
computer = random.randint(0,6)
# YOUR TURN
print('Your turn now 8')
you = int(input('Enter a number'))

win = you == computer
print(f'You won: {win}')