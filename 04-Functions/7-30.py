def sum_natural(n):
    suma = 0
    for i in range (1,n+1):
        suma += i
    return suma

if __name__ == '__main__':
    print(sum_natural(4))