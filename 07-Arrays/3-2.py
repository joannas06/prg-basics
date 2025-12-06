#An array contains natural numbers: 15, 8, 31, 47, 2, 19. 
# Create a program that prints the contents of the array in reverse order. Use any loop statement. Sample result:
#existed array: 15 8 31 47 2 19 
#reverse array: 19 2 47 31 8 15

arr1 = [15,8,31,47,2,19]

arr2 = []
for i in range(len(arr1) - 1,-1,-1):
    arr2.append(arr1[i])

print(arr1)
print(arr2)