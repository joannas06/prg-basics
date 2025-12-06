#An array contains numbers: -15, 8, -31, 47, -2, 19. 
# Create a program that finds and prints the maximum and minimum number. Do not use available functions.
arr = [-15,8,-31,47,-2,19]
maximum = arr[0]
minimum = arr[0]

# 3. Iterate through the array to compare numbers
for number in arr:
    # Check for maximum
    if number > maximum:
        maximum = number
    
    # Check for minimum
    if number < minimum:
        minimum = number

print("Maximum number:", maximum)
print("Minimum number:", minimum)