def main():
    input_data = load_input('d03_input.txt')
    solution = solve(input_data)
    print(solution)


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def solve(data):
    total_priorities = 0
    for line in data:
        compartment_a, compartment_b = split_rucksack(line.strip())
        for item in compartment_a:
            if item in compartment_b:
                total_priorities += item_priority(item)
                break
    return total_priorities


def split_rucksack(sack):
    compartment_size = int(len(sack)/2)
    return sack[:compartment_size], sack[compartment_size:]


def item_priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


if __name__ == '__main__':
    main()
