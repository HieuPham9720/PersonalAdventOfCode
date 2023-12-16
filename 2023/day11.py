grid = []

with open("day11_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        grid.append(line)
        # Expansion for horizontal line
        if "#" not in line:
            grid.append(line)

# Expansion for vertical line

# Start by flipping the matrix by its diagonal to turn columns into rows
grid = [''.join(s) for s in zip(*grid)]

# Expand
new_grid = []
for line in grid:
    new_grid.append(line)
    if "#" not in line:
        new_grid.append(line)

# Flip back:
grid = [''.join(s) for s in zip(*new_grid)]

# Find list of universe coordinates:
coordinates = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            coordinates.append([i, j])

# Calculate distance sum
total = 0
for i in range(len(coordinates) - 1):
    start_x, start_y = coordinates[i]
    for j in range(i + 1, len(coordinates)):
        end_x, end_y = coordinates[j]
        total += abs(start_x - end_x) + abs(start_y - end_y)

print(total)
