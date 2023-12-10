from math import ceil

with open("input") as f:
    input_lines = f.read().splitlines()

test1_lines = """.....
.S-7.
.|.|.
.L-J.
.....""".splitlines()

test2_lines = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".splitlines()

connections = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((-1, 0), (0, 1)),
    "F": ((0, 1), (1, 0)),
}


def get_starting_position(lines):
    starting_pos = None
    for y, line in enumerate(lines):
        if starting_pos:
            break
        for x, c in enumerate(line):
            if c == "S":
                starting_pos = (x, y)
                break

    return starting_pos


def surrounding_coords(x, y, max_x, max_y):
    res = []
    if x - 1 >= 0:
        res.append((x - 1, y))
    if x + 1 <= max_x:
        res.append((x + 1, y))
    if y - 1 >= 0:
        res.append((x, y - 1))
    if y + 1 <= max_y:
        res.append((x, y + 1))
    return res


def find_loop(lines, starting_pos):
    loop = [starting_pos]
    surrounding_start = surrounding_coords(
        starting_pos[0], starting_pos[1], len(lines[0]) - 1, len(lines) - 1
    )
    for x, y in surrounding_start:
        c = lines[y][x]
        if c in connections:
            if (
                x + connections[c][0][0] == starting_pos[0]
                and y + connections[c][0][1] == starting_pos[1]
                or x + connections[c][1][0] == starting_pos[0]
                and y + connections[c][1][1] == starting_pos[1]
            ):
                loop.append((x, y))
                break

    while True:
        x, y = loop[-1]
        c = lines[y][x]

        opt1 = (x + connections[c][0][0], y + connections[c][0][1])
        opt2 = (x + connections[c][1][0], y + connections[c][1][1])

        if len(loop) > 2 and starting_pos in (opt1, opt2):
            break

        if opt1 == loop[-2]:
            loop.append(opt2)
        else:
            loop.append(opt1)

    return loop


def part1(lines):
    starting_pos = get_starting_position(lines)
    loop = find_loop(lines, starting_pos)

    return ceil(len(loop) / 2)


print(f"Part 1: {part1(input_lines)}")
