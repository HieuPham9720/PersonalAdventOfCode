with open("day1_input.txt", "r") as file:
    sum = 0
    for line in file:
        # Using 2 indeces:
        # This runs assuming that all input lines has at least 1 digit
        l = 0
        while not line[l].isdigit():
            l += 1
        r = len(line) - 1
        while not line[r].isdigit():
            r -= 1
        sum += int(line[l] + line[r])

    print(sum)