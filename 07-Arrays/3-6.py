#An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints the array and the arithmetic mean of array values. 
# Use the “while” loop statement.
arr = [15, 8, 31, 47, 2, 19]
i = 0
total = 0
how_many = 0

while i < len(arr):
    # 1. Add the value from the array at index i
    total += arr[i]
    
    # 2. Increment the count
    how_many += 1
    
    # 3. Move to the next index LAST
    i += 1 

arithmetic_mean = total / how_many
print(arithmetic_mean)