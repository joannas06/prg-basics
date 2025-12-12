def create_2d_arr(x,y):
    arr = [[0] * x for _ in range(y)]
    return arr

if __name__ == '__main__':
    print(create_2d_arr(3,5))