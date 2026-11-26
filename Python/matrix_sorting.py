rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

total_elements = rows * cols
print(f"\nPlease enter {total_elements} numbers one by one:")

flat_list = []
for i in range(total_elements):
    val = int(input(f"Enter number {i + 1}: "))
    flat_list.append(val)

original_2d = []
index = 0
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(flat_list[index])
        index += 1
    original_2d.append(row)

print("\nOriginal 2D Array:")
for row in original_2d:
    print(row)

n = len(flat_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if flat_list[j] > flat_list[j + 1]:
            temp = flat_list[j]
            flat_list[j] = flat_list[j + 1]
            flat_list[j + 1] = temp

new_2d_array = []
index = 0
for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(flat_list[index])
        index += 1
    new_2d_array.append(new_row)

print("\nNew 2D Array with Numbers in Ascending Order:")
for row in new_2d_array:
    print(row)