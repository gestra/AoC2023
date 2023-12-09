with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()


def part1(lines):
    result = 0
    parsed_lines = []

    for line in lines:
        parsed = [int(x) for x in line.split()]
        parsed_lines.append(parsed)

    for line in parsed_lines:
        line_diffs = [line.copy()]
        target = line
        while True:
            diffs = []
            for i in range(len(target) - 1):
                diffs.append(target[i + 1] - target[i])
            line_diffs.append(diffs)
            if all(x == 0 for x in diffs):
                break
            target = diffs

        for i in range(len(line_diffs) - 1, -1, -1):
            line_diffs[i - 1].append(line_diffs[i - 1][-1] + line_diffs[i][-1])

        result += line_diffs[0][-1]

    return result


def part2(lines):
    result = 0
    parsed_lines = []

    for line in lines:
        parsed = [int(x) for x in line.split()]
        parsed_lines.append(parsed)

    for line in parsed_lines:
        line_diffs = [line.copy()]
        target = line
        while True:
            diffs = []
            for i in range(len(target) - 1):
                diffs.append(target[i + 1] - target[i])
            line_diffs.append(diffs)
            if all(x == 0 for x in diffs):
                break
            target = diffs

        for i in range(len(line_diffs) - 1, -1, -1):
            line_diffs[i - 1].insert(0, line_diffs[i - 1][0] - line_diffs[i][0])

        result += line_diffs[0][0]

    return result


print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
