#Create a program that computes the second power of each array element. Sample result:
#Array: 8 2 5 1 9
#2nd power: 64 4 25 1 81

arr1=[8,2,5,1,9]

arr2=[]

for i in arr1:
    i = i**2
    arr2.append(i)

print(*arr1)
print(*arr2)