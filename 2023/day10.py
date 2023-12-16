grid = []

start_coordinate = []

with open("day10_input.txt", "r") as input_file:
    for i, line in enumerate(input_file):
        line = line.strip()
        grid.append(line)
        for j, char in enumerate(line):
            if char = "S":
                start_coordinate = [i, j]
        


"""Algorithm:
- Each pipe is connect to only 2 other pipe, depends on shape
- Determine shape of S
- BFS
    - Look in 4 directions for applicable pipes:
        - Up: |, F, 7
        - Left: -, F, L
        - Down: |, L, J
        - Right: -, 7, J
    
- Store state of move: [current_char, last_direction]. For example:
    - ["F", "up"] -> go right   ||  ["F", "left"] -> go down
"""