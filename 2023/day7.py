total = 0

# Map to letter value for string comparison purpose ('A' > '9')
convert_map = {
    "J": "1",
    "T": "A",
    "Q": "C",
    "K": "D",
    "A": "E",
}

# Mapping from a hand to it's bid
# Entry example: 
# "hand": bid
hand_to_bid = {}

# List of hands filtered by hand type
hand_types = {
    "high_card": [],
    "one_pair": [],
    "two_pairs": [],
    "three_of_a_kind": [],
    "full_house": [],
    "four_of_a_kind": [],
    "five_of_a_kind": [],
}

def convert(hand):
    tmp = ""
    for char in hand:
        if char in convert_map:
            tmp += convert_map[char]
        else:
            tmp += char
    return tmp


with open("day7_input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        hand, bid = line.split(" ")
        hand_to_bid[hand] = int(bid)

    # Put hand in into their types
    for hand in hand_to_bid:
        card_map = {}
        for card in hand:
            card_map[card] = card_map.get(card, 0) + 1
    
        joker_count = card_map.get("J", 0)
        hand_type = ""

        # For the comments, the first number is the joker_count
        match len(card_map.values()):
            case 1:
                hand_type = "five_of_a_kind"
            case 2:
                match joker_count:
                    case 0:
                        if max(card_map.values()) == 4:     # 0 + 4/1
                            hand_type = "four_of_a_kind"
                        else:                               # 0 + 3/2
                            hand_type = "full_house"
                    case _:                                 
                        hand_type = "five_of_a_kind"        
            case 3:
                match joker_count:
                    case 0:
                        if max(card_map.values()) == 3:     # 0 + 3/1/1
                            hand_type = "three_of_a_kind"
                        else:                               # 0 + 2/2/1
                            hand_type = "two_pairs"
                    case 1:
                        if max(card_map.values()) == 3:     # 1 + 3/1
                            hand_type = "four_of_a_kind"
                        else:                               # 1 + 2/2
                            hand_type = "full_house"
                    case _:
                        hand_type = "four_of_a_kind"        # 3 + 1/1 or 2 + 2/1
            case 4:
                match joker_count:
                    case 0:                                 # 0 + 2/1/1/1
                        hand_type = "one_pair"
                    case _:                                 # 1 + 2/1/1 or 2 + 1/1/1
                        hand_type = "three_of_a_kind"
            case 5:
                hand_type = "one_pair" if joker_count == 1 else "high_card"
        
        hand_types[hand_type].append(hand)

     # Sort the hand for each hand type   
    for hand_type_list in hand_types:
        hand_types[hand_type_list].sort(
            key=lambda hand: convert(hand)
        )

    final_list = [
        *hand_types["high_card"], 
        *hand_types["one_pair"],
        *hand_types["two_pairs"],
        *hand_types["three_of_a_kind"],
        *hand_types["full_house"],
        *hand_types["four_of_a_kind"],
        *hand_types["five_of_a_kind"],
    ]

    for index, hand in enumerate(final_list):
        total += (index + 1) * hand_to_bid[hand]

    print(total)


"""Goal
- Sorting by how strong a hand is
    - Fit each hand into a type
    - Calculate the ranking from smallest to biggest
"""