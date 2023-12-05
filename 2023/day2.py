import numpy as np

with open("day2_input.txt", "r") as file:
    sum = 0
    for index, line in enumerate(file):
        line = line.rstrip()
        colon_index = line.index(":")
        grabs = line[colon_index + 2:].split("; ")
        max_color = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }  
        for grab in grabs:
            clues = grab.split(", ")
            for clue in clues:
                number, color = clue.split(" ")
                max_color[color] = max(max_color[color], int(number))
        product = 1
        for value in max_color.values():
            product *= value
        sum += product
    print(sum)