grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ] 

for i in range(5):
    for j in range(5):
        grid[i][j] = (i + 1) * (j + 1)

for row in grid:
    for num in row:
        print(f"{num:2}", end=" ")
    print()