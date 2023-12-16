patterns = []
pattern = []

with open("day13_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        if len(line) == 0:
            # Added blank line to EOF for this to work
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

result = 0

for pattern in patterns:
    largest_horizontal_pattern_size = 0
    largest_vertical_pattern_size = 0

    # Index of the row exactly above the line
    horizontal_line_index = 0
    # Index of the column exactly to the left of the line
    vertical_line_index = 0

    # Horizontal line search:
    found = False
    start = pattern[0]
    r = len(pattern) - 1
    while not found and r > 0:
        if pattern[r] == start:
            found = True
            if largest_horizontal_pattern_size < r + 1:
                largest_horizontal_pattern_size = r + 1
                horizontal_line_index = (r + 1) // 2
        r -= 1
    
    found = False
    start = pattern[-1]
    l = 0
    while not found and l < len(pattern) - 1:
        if pattern[l] == start:
            found = True
            if largest_horizontal_pattern_size < len(pattern) - l: 
                # Specifically: len(pattern) - 1 - l + 1
                largest_horizontal_pattern_size = len(pattern) - l
                horizontal_line_index = (len(pattern) - l) // 2
        l += 1
        
    # Vertical line search by flipping the pattern sideway
    pattern = ["".join(s) for s in zip(*pattern)]

    found = False
    start = pattern[0]
    r = len(pattern) - 1
    while not found and r > 0:
        if pattern[r] == start:
            found = True
            if largest_vertical_pattern_size < r + 1:
                largest_vertical_pattern_size = r + 1
                vertical_line_index = (r + 1) // 2
        r -= 1
    
    found = False
    start = pattern[-1]
    l = 0
    while not found and l < len(pattern) - 1:
        if pattern[l] == start:
            found = True
            if largest_vertical_pattern_size < len(pattern) - l: 
                largest_vertical_pattern_size = len(pattern) - l
                vertical_line_index = (len(pattern) - l) // 2
        l += 1

    # Logic on what to add to result
    if largest_horizontal_pattern_size > largest_vertical_pattern_size:
        # Reflip to horizontal
        pattern = ["".join(s) for s in zip(*pattern)]
        result += (len(pattern) - horizontal_line_index) * 100
    else:
        result += len(pattern) - vertical_line_index

print(result)


"""Algorithm:
- Try horizontal, then vertical line
- For perfect reflection, the start line must be either the first or last line
    - Try first, then go find reflection with two-pointers. If not, try last.
    - Find the largest reflection possible, bith horizontal and vertical
- Get the line location using MATH -> result
"""