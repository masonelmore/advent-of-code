def solve(data):
    total_priorities = 0
    for sack_a, sack_b, sack_c in rucksack_groups(data):
        for item in sack_a:
            if item in sack_b and item in sack_c:
                total_priorities += item_priority(item)
                break
    return total_priorities


def rucksack_groups(rucksacks):
    for rucksack in rucksacks:
        group = [rucksack, next(rucksacks), next(rucksacks)]
        yield group


def item_priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27
