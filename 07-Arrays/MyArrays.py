def secondlargest(array):
    asorted = sorted(set(array))
    return asorted[-2]

def roznica(array):
    unique_sorted = sorted(set(array))
    return unique_sorted[0]-unique_sorted[-1]

def median(array):
    array.sort()
    n = len(array)
    mid_index = n // 2
    # 2. Check if the length is Odd or Even
    if n % 2 != 0:
        # ODD: The median is simply the middle number
        return array[mid_index-1]
    else:
        # EVEN: The median is the average of the two middle numbers
        # We need the number at mid_index and the one before it
        val1 = array[mid_index - 1]
        val2 = array[mid_index]
        return (val1 + val2) / 2

def smallargearr(array):
    newarr = []
    newarr.append(array[0])
    newarr.append(array[-1])
    return newarr

def separated(array):
    newarr = []
    for i in array:
        i = str(i)
        newarr.append(i)
    delimiter = '-'

    return delimiter.join(newarr)

