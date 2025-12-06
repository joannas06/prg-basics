#An array contains values: 15, 8, 31, 47, 2, 19. 
# Create a program that calculates and prints the array and the arithmetic mean of array values. Use the “for” loop statement.

arr = [15,8,31,47,2,19]
numbers_total = 0
how_many = 0
for i in arr:
    numbers_total += i
    how_many += 1

arithmetic_mean = numbers_total/how_many

print(arithmetic_mean)