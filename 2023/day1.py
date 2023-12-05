import re

with open("day1_input.txt", "r") as file:
    sum = 0
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in file:
        # two-index to find the first and last digit
        first = last = ""
        l = 0
        while not line[l].isdigit():
            l += 1
        first = line[l]

        r = len(line) - 1
        while not line[r].isdigit():
            r -= 1
        last = line[r]

        # Find the digits in word form
        for number in numbers:
            for match in re.finditer(number, line):
                index = match.start()
                if index < l:
                    l = index
                    first = numbers[number]
                if index > r:
                    r = index
                    last = numbers[number]
        sum += int(first + last)

    print(sum)