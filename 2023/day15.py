with open("day15_input.txt", "r") as input_file:
    sequences = input_file.readline().split(",")

def get_box_number(sequence):
    value = 0
    for char in sequence:
        value += ord(char)
        value *= 17
        value = value % 256
    return value

"""TIL
boxes = [{}] * 256 will create 256 reference to the same dictionary
"""

boxes = []
for _ in range(256):
    boxes.append({})

for sequence in sequences:
    if "-" in sequence:
        label = sequence.split("-")[0]
        box = boxes[get_box_number(label)]
        if label in box:
            i = 0
            while i < len(box.keys()) and list(box.keys())[i] != label:
                del box[list(box.keys())[i]]
                i += 1
            del box[label]
    else:
        label, focal_length = sequence.split("=")
        box = boxes[get_box_number(label)]
        box[label] = int(focal_length)

print(boxes)

total_focusing_power = 0

for index, box in enumerate(boxes):
    for slot, focal_length in enumerate(box.values()):
        total_focusing_power += (index + 1) * (slot + 1) * focal_length

print(total_focusing_power)