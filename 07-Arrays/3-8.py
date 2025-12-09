arr = [2,6,4,9,7]

def star(n):
    stars = ""
    for i in range(n):
        stars += '*'
    return stars
    

if __name__ == '__main__':
    for n in arr:
        print(star(n))