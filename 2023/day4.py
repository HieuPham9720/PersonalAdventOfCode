total = 0

with open("day4_input.txt", "r") as file:
    for line in file:
        # Remove all extra spaces
        line = " ".join(line.split())
        numbers = line.split(":")[1]
        winning, scratch = numbers.split("|")
        winning_numbers = [int(num) for num in winning.strip().split(" ")]
        scratch_numbers = [int(num) for num in scratch.strip().split(" ")]
        match_count = 0
        for number in scratch_numbers:
            if number in winning_numbers:
                match_count += 1
        if match_count > 0:
            total += pow(2, match_count - 1)

print(total)


    
