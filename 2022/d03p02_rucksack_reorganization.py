def main():
    input_data = load_input('d03_input.txt')
    solution = solve(input_data)
    print(solution)


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def solve(data):
    total_priorities = 0
    for sack_a, sack_b, sack_c in rucksack_groups(data):
        for item in sack_a:
            if item in sack_b and item in sack_c:
                total_priorities += item_priority(item)
                break
    return total_priorities


def rucksack_groups(rucksacks):
    rucksacks_iter = iter(rucksacks)
    for rucksack in rucksacks_iter:
        group = [rucksack, next(rucksacks_iter), next(rucksacks_iter)]
        yield group


def item_priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


if __name__ == '__main__':
    main()
