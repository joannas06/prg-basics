arr = [2,3,2,5,8,1,9,8]

def get_unique_elements(array):
    result = []
    for n in array:
        # Check if the number appears exactly once in the list
        if array.count(n) == 1:
            result.append(n)
    return result

        
if __name__ == '__main__':
    print(get_unique_elements(arr))