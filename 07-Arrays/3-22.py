import random
arr = [1,2,3,5,6,7,8,9,0]
def rand_elem(array):
    i = random.randint(1,len(array))
    return array[i]

how_many = 5

while how_many > 0:
    how_many -= 1
    print(rand_elem(arr))