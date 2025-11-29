def liczymyliterki(n):
    counte = 0
    for letter in n:
        if letter == 'e':
            counte +=1
    return counte

if __name__ == '__main__':
    n = input('Podaj zdanie lub slowo: ')
    print(f'Tyle jest liter e: {liczymyliterki(n)}')