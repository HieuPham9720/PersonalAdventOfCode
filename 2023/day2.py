with open("day2_input.txt", "r") as file:
    sum = 0
    restraint = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for index, line in enumerate(file):
        # String manipulation for each clue in each game
        # if clue exceeds 12 red, 13 green or 14 blue then skip
        line = line.rstrip()
        colon_index = line.index(":")
        grabs = line[colon_index + 2:].split("; ")
        valid = True
        for grab in grabs:
            clues = grab.split(", ")
            for clue in clues:
                number, color = clue.split(" ")
                if restraint[color] < int(number):
                    valid = False
                    break
        if valid:
            sum += (index + 1)
    print(sum)