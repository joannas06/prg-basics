def occurs(number,array):
    check = 0
    for i in array:
        if i == number:
            check += 1
        
    if check >= 1:
        return True
    else:
        return False
    

arr = [15,38,7,23,14]

if __name__ == '__main__':
    print(occurs(23,arr))
