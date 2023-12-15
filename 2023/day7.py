total = 0

convert_map = {
    "T": "A",
    "J": "B",
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
        
        if len(card_map.values()) == 1:
            hand_types["five_of_a_kind"].append(hand)
        elif len(card_map.values()) == 2:
            if max(card_map.values()) == 4:
                hand_types["four_of_a_kind"].append(hand)
            else:
                hand_types["full_house"].append(hand)
        elif len(card_map.values()) == 3:
            if max(card_map.values()) == 3:
                hand_types["three_of_a_kind"].append(hand)
            else:
                hand_types["two_pairs"].append(hand)
        elif len(card_map.values()) == 4:
            hand_types["one_pair"].append(hand)
        else:
            hand_types["high_card"].append(hand)

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