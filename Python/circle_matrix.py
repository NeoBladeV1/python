n = int(input('Enter the size of the matrix: '))

a = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1
target = n * n

while num <= target:
    i = left
    while i<= right:
        a[top][i] = num
        num += 1
        i += 1
    top += 1

    i = top
    while i<= bottom:
        a[i][right] = num
        num += 1
        i += 1
    right -= 1

    if top <= bottom:
        i = right
        while i >= left:
            a[bottom][i] = num
            num += 1
            i -= 1
        bottom -= 1

    if left <= right:
        i = bottom
        while i >= top:
            a[i][left] = num
            num += 1
            i -= 1
        left += 1

#took help from ai
row_idx = 0
while row_idx < n:
    col_idx = 0
    while col_idx < n:
        val = a[row_idx][col_idx]
        print(val, end=" ")
        col_idx += 1
    print()
    row_idx += 1

