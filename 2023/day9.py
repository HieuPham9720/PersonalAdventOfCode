result = 0

with open("day9_input.txt", "r") as file:
    for line in file:
        start_sequence = [int(x) for x in line.strip().split(" ")]
        sequences = [start_sequence]
        while not all(val == 0 for val in start_sequence):
            new_sequence = []
            for i in range(len(start_sequence) - 1):
                new_sequence.append(start_sequence[i + 1] - start_sequence[i])
            start_sequence = new_sequence
            sequences.append(start_sequence)

        # Go through all the past sequences to find new prediction
        for j in range(len(sequences) - 1, 0, -1):
            sequences[j - 1].append(sequences[j - 1][-1] + sequences[j][-1])
        
        result += sequences[0][-1]

print(result)