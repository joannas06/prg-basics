def compare(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    else:
        for n in range(len(arr1)):
            if arr1[n] != arr2[n]:
                return False
    return True
            


words1 = ["water","book","sky"]
words2 = ["water","book","sky"]
true1 = [True,False,True]
true2 = [True,False,False]
if __name__ == '__main__':
    print(compare(words1,words2))
    print(compare(true1,true2))