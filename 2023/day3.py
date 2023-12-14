grid = []

with open("day3_input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

def is_gear(char):
    return char == "*"

# Mapping from a gear coordinates to a list of nearby numbers
# Key is a string "X,Y", value is the list of number
gear_map = {}

def add_to_gear_map(x, y, number):
    key_string = f"{x},{y}"
    if not gear_map.get(key_string, False):
        gear_map[key_string] = [number]
    else:
        gear_map[key_string].append(number)

for i, line in enumerate(grid):
    j = 0
    while j < len(line):
        if line[j].isdigit():
            # Construct the number:
            start = j
            while j < len(line) and line[j].isdigit():
                j += 1

            end = j     # end index is not inclusive

            number = int(line[start:end])
            
            # On the left
            if start > 0 and is_gear(grid[i][start - 1]):
                add_to_gear_map(i, start - 1, number)
            # On the right
            if end < len(line) and is_gear(grid[i][end]):
                add_to_gear_map(i, end, number)

            # Top left
            if i > 0 and start > 0 and is_gear(grid[i - 1][start - 1]):
                add_to_gear_map(i - 1, start - 1, number)
            # Bottom left
            if i < len(grid) - 1 and start > 0 and is_gear(grid[i + 1][start - 1]):
                add_to_gear_map(i + 1, start - 1, number)
            # Top right
            if i > 0 and end < len(line) and is_gear(grid[i - 1][end]):
                add_to_gear_map(i - 1, end, number)
            # Bottom right
            if i < len(grid) - 1 and end < len(line) and is_gear(grid[i + 1][end]):
                add_to_gear_map(i + 1, end, number)

            # Mid number
            for index in range(start, end):
                if i > 0 and is_gear(grid[i - 1][index]):
                    add_to_gear_map(i - 1, index, number)
                if i < len(grid) - 1 and is_gear(grid[i + 1][index]):
                    add_to_gear_map(i + 1, index, number)

        j += 1

total = 0

for number_list in gear_map.values():
    if len(number_list) == 2:
        total += number_list[0] * number_list[1]

print(total)


""" Steps
- Find the number
    - Find a digit
    - Keep going until non-digit/end of line
    - Saves the first and last digit coordinates
- Look around for gear symbol
    - Look up-left, left, down-left
    - Look up-right, right, down-right
    - For all digits, look up and down only
"""