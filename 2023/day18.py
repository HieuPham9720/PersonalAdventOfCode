directions = []
moves []

with open("day18_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        direction, move, color = line.split(" ")
        directions.append(direction)
        moves.append(moves)