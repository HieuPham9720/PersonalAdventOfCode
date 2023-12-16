with open("day15_input.txt", "r") as input_file:
    sequences = input_file.readline().split(",")

total = 0
for sequence in sequences:
    current = 0
    for char in sequence:
        current += ord(char)
        current *= 17
        current = current % 256
    total += current

print(total)
        