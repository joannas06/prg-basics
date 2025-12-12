x = int(input('Podaj liczbe: '))
arr = [1,5,4,2,8,12,3]
counter = 0
for i in arr:
    if i > x:
        counter += 1

print(counter)