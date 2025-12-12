# 1. Define the array as shown in the image
numbers = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

# 2. Initialize variables to track values and locations.
# We start by assuming the first item (0,0) is both the min and max.
min_val = numbers[0][0]
min_row, min_col = 0, 0

max_val = numbers[0][0]
max_row, max_col = 0, 0

# 3. Iterate through the array using nested loops
# 'i' represents the row index
for i in range(len(numbers)):
    # 'j' represents the column index inside that row
    for j in range(len(numbers[i])):
        
        current_val = numbers[i][j]
        
        # Check if the current number is smaller than our record
        if current_val < min_val:
            min_val = current_val
            min_row = i
            min_col = j
            
        # Check if the current number is larger than our record
        if current_val > max_val:
            max_val = current_val
            max_row = i
            max_col = j

# 4. Print the results
print(f"Smallest Value: {min_val} (Row: {min_row}, Column: {min_col})")
print(f"Largest Value:  {max_val} (Row: {max_row}, Column: {max_col})")

