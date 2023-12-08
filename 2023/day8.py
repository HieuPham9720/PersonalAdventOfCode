# Map an island to it's L and R location
# Example entry: {"LCP": ["FQJ", "JGH"]}
mapping = {}
steps = ""
total_count = 0

with open("day8_input.txt", "r") as file:
    for index, line in enumerate(file):
        if index == 0:
            steps = line.strip()
        elif index == 1:
            pass
        else:
            # Since all data is in the form XXX = (XXX, XXX)
            mapping[line[:3]] = [line[7:10], line[12:15]]

current = "AAA"

while current != "ZZZ":
    for step in steps:
        current = mapping[current][0] if step == "L" else mapping[current][1]
        total_count += 1
        if current == "ZZZ":
            break

print(total_count)
