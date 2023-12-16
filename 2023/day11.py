from pprint import pprint

grid = []
empty_rows = []
empty_columns = []

with open("day11_input.txt", "r") as input_file:
    for index, line in enumerate(input_file):
        line = line.strip()
        grid.append(line)
        # Expansion for horizontal line
        if "#" not in line:
            empty_rows.append(index)

# Start by flipping the matrix by its diagonal to turn columns into rows
grid = [''.join(s) for s in zip(*grid)]

for index, line in enumerate(grid):
    if "#" not in line:
        empty_columns.append(index)

# Flip back:
grid = [''.join(s) for s in zip(*grid)]

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
        for index in empty_rows:
            if index in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                total += 999999
        for index in empty_columns:
            if index in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                total += 999999

print(total)

"""Algorithm:
- Find index of empty rows and columns
- Go through all pairs of universe:
    - Check through the list of empty rows and columns to see if any exist betweem them
    - DOMAIN EXPANSION MATH STUFF
"""