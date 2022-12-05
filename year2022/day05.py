def solve_part1(data):
    stacks = get_stacks(data)
    for qty, src, dst in get_moves(data):
        move_crates(stacks, qty, src, dst)
    top_crates = crates_at_top(stacks)
    return top_crates


def solve_part2(data):
    stacks = get_stacks(data)
    for qty, src, dst in get_moves(data):
        move_crates(stacks, qty, src, dst, keep_order=True)
    top_crates = crates_at_top(stacks)
    return top_crates


def get_stacks(data):
    stack_data = []
    for line in data:
        if not line.strip():
            break
        stack_data.append(line)

    locations = get_stack_locations(stack_data[-1])
    stack_data = stack_data[:-1]
    stacks = {}
    for stack_line in stack_data[::-1]:
        for location, index in locations.items():
            crate = stack_line[index]
            if crate == ' ':
                continue
            if not stacks.get(location):
                stacks[location] = []
            stacks[location].append(crate)
    return stacks


def get_stack_locations(locations_line):
    locations = {}
    for location in locations_line.strip().split('   '):
        index = locations_line.index(location)
        locations[location] = index
    return locations


def get_moves(data):
    for line in data:
        _, qty, _, src, _, dst = line.split(' ')
        yield int(qty), src, dst


def move_crates(stacks, qty, src, dst, keep_order=False):
    crates_to_move = stacks[src][len(stacks[src]) - qty:]
    stacks[src] = stacks[src][:-qty]

    if not keep_order:
        crates_to_move = reversed(crates_to_move)

    stacks[dst].extend(crates_to_move)


def crates_at_top(stacks):
    top_crates = ''
    for stack, crates in stacks.items():
        if not crates:
            continue
        top_crates += crates[-1]
    return top_crates
