def solve_part1(data):
    total_priorities = 0
    for line in data:
        compartment_a, compartment_b = split_rucksack(line)
        for item in compartment_a:
            if item in compartment_b:
                total_priorities += item_priority(item)
                break
    return total_priorities


def solve_part2(data):
    total_priorities = 0
    for sack_a, sack_b, sack_c in rucksack_groups(data):
        for item in sack_a:
            if item in sack_b and item in sack_c:
                total_priorities += item_priority(item)
                break
    return total_priorities


def split_rucksack(sack):
    compartment_size = int(len(sack) / 2)
    return sack[:compartment_size], sack[compartment_size:]


def rucksack_groups(rucksacks):
    for rucksack in rucksacks:
        group = [rucksack, next(rucksacks), next(rucksacks)]
        yield group


def item_priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27
