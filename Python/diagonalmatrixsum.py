n = int(input('Enter the size of the matrix: '))

matrix = []

row_idx = 0
while row_idx < n:
    print(f"Enter elements for row {row_idx + 1}:")
    row = []
    col_idx = 0
    while col_idx < n:
        val = int(input(f"Element at ({row_idx}, {col_idx}): "))
        row.append(val)
        col_idx += 1
    matrix.append(row)
    row_idx += 1

print("The entered matrix is:")
row_idx = 0
while row_idx < n:
    col_idx = 0
    while col_idx < n:
        val = matrix[row_idx][col_idx]
        print(val, end=" ")
        col_idx += 1
    print()
    row_idx += 1

main_diagonal_sum = 0
secondary_diagonal_sum = 0

i = 0
while i < n:
    main_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][n - 1 - i]
    i += 1

print(f"Sum of the main diagonal: {main_diagonal_sum}")
print(f"Sum of the secondary diagonal: {secondary_diagonal_sum}")

if main_diagonal_sum == secondary_diagonal_sum:
    print("The sums of the main and secondary diagonals are equal.")
else:
    print("The sums of the main and secondary diagonals are not equal.")

