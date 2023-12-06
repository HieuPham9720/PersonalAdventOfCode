total = 0

card_owned_count = [1] * 202    # input has 202 lines

with open("day4_input.txt", "r") as file:
    for index, line in enumerate(file):
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

        for i in range(index + 1, min(index + 1 + match_count, 202)):
            card_owned_count[i] += card_owned_count[index]

print(sum(card_owned_count))

    
