grid = []
# empty grid to count light later
final_grid = []

with open("day16_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        grid.append(line)
        final_grid.append(["."] * len(line))

current_position = [0, 0]

