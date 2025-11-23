###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    absolute = abs(number)
    string = str(absolute)
    total = 0
    for char in string:
        total += int(char)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {(any_number)} is {sum_digits(any_number)}')