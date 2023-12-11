with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()


def find_galaxies(lines):
    galaxies = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))
    return galaxies


def find_empty_rows(lines):
    empty = []
    for y, line in enumerate(lines):
        if all(c == "." for c in line):
            empty.append(y)
    return empty


def find_empty_cols(lines):
    cols = []
    for x in range(len(lines[0])):
        empty = True
        for line in lines:
            if line[x] == "#":
                empty = False
                break
        if empty:
            cols.append(x)

    return cols


def solve(lines, expansion):
    galaxies = find_galaxies(lines)
    empty_rows = find_empty_rows(lines)
    empty_cols = find_empty_cols(lines)

    pairs = []
    for i, g1 in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            pairs.append((g1, galaxies[j]))

    distances = {}
    for g1, g2 in pairs:
        dist = -2
        smaller_x = min(g1[0], g2[0])
        larger_x = max(g1[0], g2[0])
        for c in range(smaller_x, larger_x + 1):
            if c in empty_cols:
                dist += expansion
            else:
                dist += 1
        smaller_y = min(g1[1], g2[1])
        larger_y = max(g1[1], g2[1])
        for c in range(smaller_y, larger_y + 1):
            if c in empty_rows:
                dist += expansion
            else:
                dist += 1

        distances[(g1, g2)] = dist

    return sum(distances.values())


print(f"Part 1: {solve(input_lines, 2)}")
print(f"Part 2: {solve(input_lines, 1000000)}")
