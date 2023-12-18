from heapq import heappush, heappop
from collections import defaultdict

with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".splitlines()

test_lines2 = """111111111111
999999999991
999999999991
999999999991
999999999991""".splitlines()


def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path


def a_star(start, goal, neighbors, losses):
    open_set = []
    heappush(open_set, (0, (start[0], start[1], "h")))
    heappush(open_set, (0, (start[0], start[1], "v")))

    came_from = {}

    g_score = defaultdict(lambda: float("inf"))
    g_score[(start[0], start[1], "h")] = 0
    g_score[(start[0], start[1], "v")] = 0

    f_score = defaultdict(lambda: float("inf"))
    f_score[(start[0], start[1], "h")] = heuristic(start, goal)
    f_score[(start[0], start[1], "v")] = heuristic(start, goal)

    while len(open_set) > 0:
        _, current = heappop(open_set)
        if current[0] == goal[0] and current[1] == goal[1]:
            return reconstruct_path(came_from, current)

        for neighbor in neighbors[current]:
            tentative_g_score = g_score[current] + losses[(current, neighbor)]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(
                    (neighbor[0], neighbor[1]), goal
                )

                in_open_set = False
                for _, coord in open_set:
                    if coord == neighbor:
                        in_open_set = True
                        break
                if not in_open_set:
                    heappush(open_set, (f_score[neighbor], neighbor))


def preprocess(lines, min_movement, max_movement):
    neighbors = {}
    losses = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            for i in range(x - max_movement + 1, x + max_movement):
                if i == x or i < 0 or i > len(line) - 1 or abs(x - i) < min_movement:
                    continue
                if (x, y, "v") not in neighbors:
                    neighbors[(x, y, "v")] = []
                neighbors[(x, y, "v")].append((i, y, "h"))

                loss = 0
                if i < x:
                    for x0 in range(i, x):
                        loss += int(lines[y][x0])
                else:
                    for x0 in range(x + 1, i + 1):
                        loss += int(lines[y][x0])
                losses[((x, y, "v"), (i, y, "h"))] = loss
            for j in range(y - max_movement + 1, y + max_movement):
                if j == y or j < 0 or j > len(lines) - 1 or abs(y - j) < min_movement:
                    continue
                if (x, y, "h") not in neighbors:
                    neighbors[(x, y, "h")] = []
                neighbors[(x, y, "h")].append((x, j, "v"))

                loss = 0
                if j < y:
                    for y0 in range(j, y):
                        loss += int(lines[y0][x])
                else:
                    for y0 in range(y + 1, j + 1):
                        loss += int(lines[y0][x])
                losses[((x, y, "h"), (x, j, "v"))] = loss

    return neighbors, losses


def solve(lines, neighbors, losses):
    path = a_star((0, 0), (len(lines[0]) - 1, len(lines) - 1), neighbors, losses)

    path.reverse()
    loss = 0
    for i in range(len(path) - 1):
        loss += losses[(path[i], path[i + 1])]

    return loss


def part1(lines):
    neighbors, losses = preprocess(lines, 1, 4)
    return solve(lines, neighbors, losses)


def part2(lines):
    neighbors, losses = preprocess(lines, 4, 11)
    return solve(lines, neighbors, losses)


print(f"Part 1: {part1(input_lines)}")
print(f"Part 1: {part2(input_lines)}")
