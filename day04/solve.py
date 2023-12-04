with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()


def part1(lines):
    score = 0

    for line in lines:
        cardnum_split = line.split(": ")
        # card_no = int(cardnum_split[0][5:])
        winning_split = cardnum_split[1].split(" | ")
        winning_numbers = winning_split[0].split()
        my_numbers = winning_split[1].split()

        card_points = 0
        for n in my_numbers:
            if n in winning_numbers:
                if card_points > 0:
                    card_points *= 2
                else:
                    card_points = 1

        # print(f"Card {card_no} is worth {card_points}")
        score += card_points

    return score


def part2(lines):
    num_cards = [1] * len(lines)

    total_cards = 0

    for i, line in enumerate(lines):
        total_cards += num_cards[i]

        cardnum_split = line.split(": ")
        # card_no = int(cardnum_split[0][5:])
        winning_split = cardnum_split[1].split(" | ")
        winning_numbers = winning_split[0].split()
        my_numbers = winning_split[1].split()

        winning_cards = 0
        for n in my_numbers:
            if n in winning_numbers:
                winning_cards += 1
        for j in range(i+1, i+1+winning_cards):
            num_cards[j] += num_cards[i]

    return total_cards


print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
