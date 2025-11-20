###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = float(input('Enter radius: '))
PI = 3.14

# calculate area 
# Formula: PI * r^2
area = PI * (radius ** 2)

# calculate circumference 
# Formula: 2 * PI * r
circumference = 2 * PI * radius

# print results
print(f'Circle Area: {area}')
print(f'Circle Circumference: {circumference}')