with open("input") as f:
    input_lines = f.readlines()

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

def part1(lines):
    max_red = 12
    max_green = 13
    max_blue = 14

    sum = 0

    for line in lines:
        line = line.strip()
        id_split = line.split(": ")
        id = int(id_split[0][5:])

        reveals = id_split[1].split("; ")

        possible = True
        for reveal in reveals:
            dice = reveal.split(", ")
            for die in dice:
                amount_split = die.split(" ")
                amount = int(amount_split[0])
                color = amount_split[1]
                
                match color:
                    case "red":
                        if amount > max_red:
                            possible = False
                            break
                    case "green":
                        if amount > max_green:
                            possible = False
                            break
                    case "blue":
                        if amount > max_blue:
                            possible = False
                            break
                    case _:
                        print(f"ERROR: {color}")
            if not possible:
                break
                
        if possible:
            sum += id
    
    return sum

def part2(lines):
    sum = 0
    
    for line in lines:
        min_red = None
        min_green = None
        min_blue = None

        line = line.strip()
        id_split = line.split(": ")
        id = int(id_split[0][5:])

        reveals = id_split[1].split("; ")
        for reveal in reveals:
            dice = reveal.split(", ")
            for die in dice:
                amount_split = die.split(" ")
                amount = int(amount_split[0])
                color = amount_split[1]
                
                match color:
                    case "red":
                        if not min_red or amount > min_red:
                            min_red = amount
                    case "green":
                        if not min_green or amount > min_green:
                            min_green = amount
                    case "blue":
                        if not min_blue or amount > min_blue:
                            min_blue = amount
                    case _:
                        print(f"ERROR: {color}")
                
        power = min_red * min_green * min_blue
        sum += power
    
    return sum

print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")