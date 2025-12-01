def f(number):
    sum = 0
    number_str = str(number)
    for i in number_str:
        if number_str.count(i)>1:
            sum+=int(i)
    return sum

if __name__ == '__main__':
    print(f(1024))
    print(f(230335))