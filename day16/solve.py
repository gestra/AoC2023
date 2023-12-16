with open("input") as f:
    input_lines = f.read().splitlines()

test_lines = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".splitlines()

def beamstr(beam):
    return f"{beam["x"]},{beam["y"]},{beam["dir"]}"

def run_beam(lines, starting_beam):
    beams = [starting_beam]
    energized = set()
    checked_beams = set()

    while len(beams) > 0:
        beam = beams.pop()
        s = beamstr(beam)
        if s in checked_beams:
            continue
        checked_beams.add(s)
        
        match beam["dir"]:
            case "R":
                beam["x"] += 1
                if beam["x"] >= len(lines[0]):
                    continue
                energized.add((beam["x"], beam["y"]))
                match lines[beam["y"]][beam["x"]]:
                    case "|":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "U"})
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "D"})
                    case "/":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "U"})
                    case "\\":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "D"})
                    case _:
                        beams.append(beam)
            case "L":
                beam["x"] -= 1
                if beam["x"] < 0:
                    continue
                energized.add((beam["x"], beam["y"]))
                match lines[beam["y"]][beam["x"]]:
                    case "|":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "U"})
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "D"})
                    case "/":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "D"})
                    case "\\":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "U"})
                    case _:
                        beams.append(beam)
            case "U":
                beam["y"] -= 1
                if beam["y"] < 0:
                    continue
                energized.add((beam["x"], beam["y"]))
                match lines[beam["y"]][beam["x"]]:
                    case "-":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "L"})
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "R"})
                    case "/":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "R"})
                    case "\\":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "L"})
                    case _:
                        beams.append(beam)
            case "D":
                beam["y"] += 1
                if beam["y"] >= len(lines):
                    continue
                energized.add((beam["x"], beam["y"]))
                match lines[beam["y"]][beam["x"]]:
                    case "-":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "L"})
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "R"})
                    case "/":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "L"})
                    case "\\":
                        beams.append({"x": beam["x"], "y": beam["y"], "dir": "R"})
                    case _:
                        beams.append(beam)
    
    return len(energized)

def part1(lines):
    return run_beam(lines, {"x": -1, "y": 0, "dir": "R"})

def part2(lines):
    maximum = 0
    for x in range(len(lines[0])):
        energized = run_beam(lines, {"x": x, "y": -1, "dir": "D"})
        if energized > maximum:
            maximum = energized
        energized = run_beam(lines, {"x": x, "y": len(lines), "dir": "U"})
        if energized > maximum:
            maximum = energized
    for y in range(len(lines)):
        energized = run_beam(lines, {"x": -1, "y": y, "dir": "R"})
        if energized > maximum:
            maximum = energized
        energized = run_beam(lines, {"x": len(lines[0]), "y": y, "dir": "L"})
        if energized > maximum:
            maximum = energized
    
    return maximum

print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")

