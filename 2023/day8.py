import math

# Map an island to it's L and R location
# Example entry: {"LCP": ["FQJ", "JGH"]}
mapping = {}
steps = ""

with open("day8_input.txt", "r") as file:
    for index, line in enumerate(file):
        if index == 0:
            steps = line.strip()
        elif index == 1:
            pass
        else:
            # Since all data is in the form XXX = (XXX, XXX)
            mapping[line[:3]] = [line[7:10], line[12:15]]

node_moves = []
for node in mapping.keys():
    if node[2] == "A":
        step_count = 0
        while node[2] != "Z":
            for step in steps:
                node = mapping[node][0] if step == "L" else mapping[node][1]
                step_count += 1
                if node[2] == "Z":
                    break
        node_moves.append(step_count)

result = 1
for move in node_moves:
    result = math.lcm(result, move)
print(result)



"""
Alternate solution:
- For each node, find out how long it takes to reach one that ends in "Z"
- Find the least common multple of those
"""