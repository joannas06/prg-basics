###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#

swift = input('Enter SWIFT code: ')

# Extract the first 4 characters (0, 1, 2, 3)
bank_code = swift[0:4]

# Extract the next 2 characters (4, 5)
country_code = swift[4:6]

print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')