circumfrence = float(input ('Enter the trees circumfrence: '))
diameter = circumfrence / 3.14

cut_down = diameter > 50

print(f'Can this tree be cut down? {cut_down}')