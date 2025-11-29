def f(number,even):
    number = str(number)
    suma = 0
    if even == True:
        for znak in number:
            znak = int(znak)
            if znak % 2 == 0:
                suma += znak

    if even == False:
        for znak in number:
            znak=int(znak)
            if znak % 2 != 0:
                suma += znak
    return suma

if __name__ == '__main__':
    print(f(3124,True))
    print(f(3124,False))