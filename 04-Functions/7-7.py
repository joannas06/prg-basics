def f(binary_number):
    for liczba in binary_number:
        if liczba != '1' and liczba != '0':
            return False
    return True
        
if __name__ == '__main__':
    print(f('10101011110'))
    print(f('13ed11432'))