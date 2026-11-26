import array

x = array.array('i', [0] * 6)
y = array.array('i', [0] * 6)

max_distance_sq = 0
furthest_x = 0
furthest_y = 0

print("=== Coordinate Distance Calculator ===")
print("Enter 5 points (x and y coordinates):\n")

for i in range(5):
    print(f"Point {i + 1}:")
    x[i] = int(input("  Enter x: "))
    y[i] = int(input("  Enter y: "))
    
    current_distance_sq = (x[i] * x[i]) + (y[i] * y[i])
    
    if current_distance_sq > max_distance_sq:
        max_distance_sq = current_distance_sq
        furthest_x = x[i]
        furthest_y = y[i]
    print("-" * 25)

print(f"The point furthest from the origin is: ({furthest_x}, {furthest_y})")