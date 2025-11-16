###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = max(0, abs(first_letter_code - last_letter_code) - 1)
print(f'Between {first} and {last} is {number_of_letters} letters')