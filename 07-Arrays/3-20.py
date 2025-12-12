arr = [7,9,2,4,5,6]
newarr = []
twoarr = []
for i in arr:
    if i % 2 == 0:
        newarr.append(i)
    else:
        twoarr.append(i)
print(newarr+twoarr)