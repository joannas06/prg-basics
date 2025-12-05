# 6. Matrix Diagonal Replacement

# The initial square matrix with zeros
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Loop to replace diagonal values
# The main diagonal is where the row index equals the column index (0,0), (1,1), (2,2)
for i in range(len(matrix)):
    matrix[i][i] = 1

# Print the modified array
for row in matrix:
    # This prints the row cleanly without brackets, e.g., 1 0 0
    for value in row:
        print(value, end=" ")
    print() # Newline after each row