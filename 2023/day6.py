with open("day6_input.txt", "r") as file:
    ways = 0
    time = int(file.readline())
    distance = int(file.readline())
    for i in range(1, time + 1):
        if i * (time - i) > distance:
            ways += 1

print(ways)
