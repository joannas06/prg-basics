def month(n):
    if n == 1:
        return 'The Month is January'
    elif n == 2:
        return 'The Month is February'
    elif n == 3:
        return 'The Month is March'
    elif n == 4:
        return 'The Month is April'
    elif n == 5:
        return 'The Month is May'
    elif n == 6:
        return 'The Month is June'
    elif n == 7:
        return 'The Month is July'
    elif n == 8:
        return 'The Month is August'
    elif n == 9:
        return 'The Month is September'
    elif n == 10:
        return 'The Month is October'
    elif n == 11:
        return 'The Month is November'
    elif n == 12:
        return 'The Month is December'
    
if __name__ == '__main__':
    n = int(input('What is the number of the month?'))
    print(month(n))