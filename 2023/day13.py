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
    # Horizontal line search:
    found = False
    start = pattern[0]
    r = len(pattern) - 1
    while not found and r > 0:
        if pattern[r] == start:
            found = True
            result += (1 + (r + 1)) // 2 * 100
        r -= 1
    
    l = 0
    start = pattern[-1]
    while not found and l < len(pattern) - 1:
        if pattern[l] == start:
            found = True
            result += ((l + 1) + len(pattern)) // 2 * 100
        l += 1
        
    # Vertical line search by flipping the pattern sideway
    pattern = ["".join(s) for s in zip(*pattern)]
    start = pattern[0]
    r = len(pattern) - 1
    while not found and r > 0:
        if pattern[r] == start:
            found = True
            result += (1 + (r + 1)) // 2
        r -= 1
    
    l = 0
    start = pattern[-1]
    while not found and l < len(pattern) - 1:
        if pattern[l] == start:
            found = True
            result += ((l + 1) + len(pattern)) // 2
        l += 1

print(result)


"""Algorithm:
- Try horizontal, then vertical line
- For perfect reflection, the start line must be either the first or last line
    - Try first, then go find reflection with two-pointers. If not, try last.
    - Find the largest reflection possible, bith horizontal and vertical
- Get the line location using MATH -> result
"""