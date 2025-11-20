###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# input temperature
celsius = float(input('Input the temperature in celsius: '))
# transfer to fahrenheit and kelvin
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15
# print it
print(f'The temperature in Celsius is: {celsius}')
print(f'The temperature in Fahrenheit is: {fahrenheit}')
print(f'The temperature in Kelvin is: {kelvin}')