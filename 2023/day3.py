grid = []

with open("day3_input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

def is_symbol(char):
    return not char.isdigit() and char != "."

total = 0

for i, line in enumerate(grid):
    j = 0
    while j < len(line):
        if line[j].isdigit():
            # Construct the number:
            start = j
            while j < len(line) and line[j].isdigit():
                j += 1

            end = j     # end index is not inclusive

            # Check for symbol
            valid = False
            
            # On the left
            if start > 0:
                valid = valid or is_symbol(grid[i][start - 1])
            # On the right
            if end < len(line):
                valid = valid or is_symbol(grid[i][end])

            # Top left
            if i > 0 and start > 0:
                valid = valid or is_symbol(grid[i - 1][start - 1])
            # Bottom left
            if i < len(grid) - 1 and start > 0:
                valid = valid or is_symbol(grid[i + 1][start - 1])
            # Top right
            if i > 0 and end < len(line):
                valid = valid or is_symbol(grid[i - 1][end])
            # Bottom right
            if i < len(grid) - 1 and end < len(line):
                valid = valid or is_symbol(grid[i + 1][end])

            # Mid number
            for index in range(start, end):
                if i > 0:
                    valid = valid or is_symbol(grid[i - 1][index])
                if i < len(grid) - 1:
                    valid = valid or is_symbol(grid[i + 1][index])

            if valid:
                total += int(line[start:end])
        j += 1

print(total)

""" Steps
- Find the number
    - Find a digit
    - Keep going until symbol/end of line
    - Saves the first and last digit coordinates
- Look around for non-peiod symbol
    - Look up-left, left, down-left
    - Look up-right, right, down-right
    - For all digits, look up and down only
"""