arr = [1,4,5,6,7,3,9,8]
arr2 = [12,7,34,53,25,56,44,45]
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array


if __name__ == '__main__':
    print(bubblesort(arr))
    print(bubblesort(arr2))