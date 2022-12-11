def solve_part1(data):
    unique_visits = follow_head(data, knots=2)
    return len(unique_visits)


def solve_part2(data):
    unique_visits = follow_head(data, knots=10)
    return len(unique_visits)


def follow_head(data, knots):
    rope = [{'x': 0, 'y': 0} for _ in range(knots)]
    head = rope[0]
    tail = rope[-1]
    visited = set()
    visit(visited, tail)

    for vec, distance in parse_moves(data):
        for _ in range(distance):
            move(head, vec)
            prev = head
            for knot in rope[1:]:
                follow(knot, prev)
                prev = knot
            visit(visited, tail)

    return visited


def visit(visited, pos):
    visited.add(f'{pos["x"]},{pos["y"]}')


def parse_moves(data):
    directions = {
        'U': {'x': 0, 'y': -1},
        'D': {'x': 0, 'y': 1},
        'L': {'x': -1, 'y': 0},
        'R': {'x': 1, 'y': 0},
    }

    for line in data:
        parts = line.split(' ')
        direction = directions[parts[0]]
        distance = int(parts[1])
        yield direction, distance


def move(pos, vec):
    pos['x'] += vec['x']
    pos['y'] += vec['y']


def follow(src, dst):
    dx = dst['x'] - src['x']
    dy = dst['y'] - src['y']
    vec = {'x': 0, 'y': 0}

    # src ahead of dst
    if dx > 1:
        vec['x'] = dx - 1
    # src behind dst
    elif dx < -1:
        vec['x'] = dx + 1

    # src above dst
    if dy > 1:
        vec['y'] = dy - 1
    # src below dst
    elif dy < -1:
        vec['y'] = dy + 1

    # dumb hack for half-diagonal move
    # there has to be a more elegant way, but I'm not seeing it
    # The numbers Mason! What do they mean?!
    if abs(dx) == 2 and abs(dy) == 1:
        vec['y'] = dy
    elif abs(dy) == 2 and abs(dx) == 1:
        vec['x'] = dx

    move(src, vec)
