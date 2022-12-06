def solve_part1(data):
    line = next(data)
    for i in range(4, len(line)):
        window = set(line[i - 4:i])
        if len(window) == 4:
            return i


def solve_part2(data):
    line = next(data)
    for i in range(14, len(line)):
        window = set(line[i - 14:i])
        if len(window) == 14:
            return i
