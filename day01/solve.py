with open("input") as f:
    input = f.readlines()


def part1():
    sum = 0

    for line in input:
        for c in line:
            if c.isnumeric():
                first = c
                break
        for c in reversed(line):
            if c.isnumeric():
                last = c
                break
        number = int(f"{first}{last}")
        sum += number
    return sum


def part2():
    sum = 0

    for line in input:
        line = line.strip()
        for i, c in enumerate(line):
            if c.isnumeric():
                first_digit_i = i
                first = c
                break
        for i in range(first_digit_i):
            if line[i:].startswith("one"):
                first = "1"
                break
            elif line[i:].startswith("two"):
                first = "2"
                break
            elif line[i:].startswith("three"):
                first = "3"
                break
            elif line[i:].startswith("four"):
                first = "4"
                break
            elif line[i:].startswith("five"):
                first = "5"
                break
            elif line[i:].startswith("six"):
                first = "6"
                break
            elif line[i:].startswith("seven"):
                first = "7"
                break
            elif line[i:].startswith("eight"):
                first = "8"
                break
            elif line[i:].startswith("nine"):
                first = "9"
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isnumeric():
                last_digit_i = i
                last = line[i]
                break
        for i in range(last_digit_i, len(line)):
            if line[i:].startswith("one"):
                last = "1"
            elif line[i:].startswith("two"):
                last = "2"
            elif line[i:].startswith("three"):
                last = "3"
            elif line[i:].startswith("four"):
                last = "4"
            elif line[i:].startswith("five"):
                last = "5"
            elif line[i:].startswith("six"):
                last = "6"
            elif line[i:].startswith("seven"):
                last = "7"
            elif line[i:].startswith("eight"):
                last = "8"
            elif line[i:].startswith("nine"):
                last = "9"
        number = int(f"{first}{last}")
        sum += number
    return sum


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
