with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

def adjacent_coords(coords, max_x, max_y):
    to_check = []
    for x, y in coords:
        to_check.append((x - 1, y - 1))
        to_check.append((x, y - 1))
        to_check.append((x + 1, y - 1))

        to_check.append((x - 1, y))
        to_check.append((x + 1, y))

        to_check.append((x - 1, y + 1))
        to_check.append((x, y + 1))
        to_check.append((x + 1, y + 1))
    to_check = list(
        set(
            filter(
                lambda c: c[0] >= 0
                and c[1] >= 0
                and c[0] <= max_x
                and c[1] <= max_y,
                to_check,
            )
        )
    )

    return to_check

def adjacent_is_symbol(lines: list[str], coords: list[(int, int)]):
    to_check = adjacent_coords(coords, len(lines)-1, len(lines[0])-1)
    for x, y in to_check:
        if (not lines[y][x].isnumeric()) and (lines[y][x] != "."):
            return True

    return False

def find_numbers(lines):
    numbers = []
    num = {"digits": "", "coords": []}
    for l_i, line in enumerate(lines):
        if len(num["digits"]) > 0:
            numbers.append(num)
            num = {"digits": "", "coords": []}
        for c_i, c in enumerate(line):
            if c.isnumeric():
                num["digits"] += c
                num["coords"].append((c_i, l_i))
            else:
                if len(num["digits"]) > 0:
                    numbers.append(num)
                    num = {"digits": "", "coords": []}
    if len(num["digits"]) > 0:
        numbers.append(num)
    
    return numbers

def part1(lines: list[str]):
    numbers = find_numbers(lines)

    res = 0
    for n in numbers:
        if adjacent_is_symbol(lines, n["coords"]):
            res += int(n["digits"])

    return res

def part2(lines):
    numbers = find_numbers(lines)
    
    stars = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '*':
                stars.append((x, y))
    
    sum = 0
    for star in stars:
        adjacent_numbers = []
        for n in numbers:
            adjacent = adjacent_coords(n["coords"], len(lines)-1, len(lines[0])-1)
            for c in adjacent:
                if c == star:
                    adjacent_numbers.append(n)
                    break
        
        if len(adjacent_numbers) == 2:
            sum += int(adjacent_numbers[0]["digits"]) * int(adjacent_numbers[1]["digits"])
    
    return sum
            
    
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
