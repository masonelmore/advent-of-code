def solve_part1(data):
    fully_overlapping = 0
    for section_a, section_b in section_assignments(data):
        if full_overlap(section_a, section_b):
            fully_overlapping += 1
    return fully_overlapping


def solve_part2(data):
    partial_overlapping = 0
    for section_a, section_b in section_assignments(data):
        if partial_overlap(section_a, section_b):
            partial_overlapping += 1
    return partial_overlapping


def section_assignments(data):
    for line in data:
        range_a, range_b = line.split(',')
        ids_a = section_ids(range_a)
        ids_b = section_ids(range_b)
        yield ids_a, ids_b


def section_ids(section_range):
    start, end = section_range.split('-')
    ids = list(range(int(start), int(end) + 1))
    return ids


def full_overlap(section_a, section_b):
    a, b = set(section_a), set(section_b)
    return a.issubset(b) or b.issubset(a)


def partial_overlap(section_a, section_b):
    a, b = set(section_a), set(section_b)
    return not a.isdisjoint(b)
