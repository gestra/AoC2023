with open("input") as f:
    input_file = f.read().strip()

test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def hash(s: str):
    value = 0

    for c in s:
        value += ord(c)
        value *= 17
        value = value % 256

    return value


def part1(line):
    steps = line.split(",")
    hashes = map(hash, steps)

    return sum(hashes)


def part2(line):
    steps = line.split(",")
    boxes = []
    for _ in range(256):
        boxes.append([])

    for step in steps:
        if step[-1] == "-":
            label = step[:-1]
            boxno = hash(label)
            for i, lense in enumerate(boxes[boxno]):
                if lense["label"] == label:
                    del boxes[boxno][i]
                    break
        else:
            s = step.split("=")
            label = s[0]
            boxno = hash(label)
            focal_length = int(s[1])
            found = False
            for i in range(len(boxes[boxno])):
                if boxes[boxno][i]["label"] == label:
                    boxes[boxno][i]["focal_length"] = focal_length
                    found = True
                    break
            if not found:
                boxes[boxno].append({"label": label, "focal_length": focal_length})

    power = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            power += (i + 1) * (j + 1) * lens["focal_length"]

    return power


print(f"Part 1: {part1(input_file)}")
print(f"Part 2: {part2(input_file)}")
