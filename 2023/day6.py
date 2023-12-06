result = 1

with open("day6_input.txt", "r") as file:
    times_line = file.readline()
    # oneliner just for fun this time :)
    times = " ".join(times_line.strip().split()).split(": ")[1].split(" ")
    distances_line = file.readline()
    distances = " ".join(distances_line.strip().split()).split(": ")[1].split(" ")
    
    for time, distance in zip(times, distances):
        time = int(time)
        distance = int(distance)
        ways_to_win = 0
        greater = False
        for i in range(1, time + 1):
            if i * (time - i) > distance:
                greater = True
                ways_to_win += 1
            elif greater:
                break
        result *= ways_to_win
        print(ways_to_win)

print(result)
        

