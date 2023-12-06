with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = """Time:      7  15   30
Distance:  9  40  200""".splitlines()


def part1(lines):
    races = []
    for time, distance in zip(lines[0].split()[1:], lines[1].split()[1:]):
        races.append({"time": int(time), "distance": int(distance)})

    result = 1
    for race in races:
        ways = 0
        for hold in range(1, race["time"]):
            speed = hold
            remaining_time = race["time"] - hold
            distance = speed * remaining_time
            if distance > race["distance"]:
                ways += 1
        result *= ways

    return result


def part2(lines):
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))

    ways = 0
    for hold in range(1, time):
        speed = hold
        remaining_time = time - hold
        d = speed * remaining_time
        if d > distance:
            ways += 1

    return ways


print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
