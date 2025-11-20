###
# A program that reads an integer number from the keyboard
# and prints that value as a binary and hexadecimal number.
#

number = int(input("Enter number: "))

# Convert to binary (base 2)
# The result starts with '0b'
binary_number = bin(number)

# Convert to hexadecimal (base 16)
# The result starts with '0x'
hex_number = hex(number)

print(f"Binary number: {binary_number}")
print(f"Hexadecimal number: {hex_number}")