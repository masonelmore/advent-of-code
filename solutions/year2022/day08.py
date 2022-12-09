def solve_part1(data):
    grid = load_grid(data)
    width = len(grid[0])
    height = len(grid)
    visible = visible_perimeter(width, height)
    visible += visible_interior(grid, width, height)
    return visible


def solve_part2(data):
    grid = load_grid(data)
    score = highest_scenic_score(grid)
    return score


def load_grid(data):
    grid = []
    for line in data:
        row = []
        for cell in line:
            row.append(int(cell))
        grid.append(row)
    return grid


def visible_perimeter(width, height):
    # -4 to remove the shared corners
    return width * 2 + height * 2 - 4


def visible_interior(grid, width, height):
    visible = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if is_visible(grid, width, height, x, y):
                visible += 1
    return visible


def is_visible(grid, w, h, x, y):
    directions = [
        {'x': -1, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 0, 'y': -1},
        {'x': 0, 'y': 1},
    ]

    cell = grid[y][x]
    is_blocked = 0
    for d in directions:
        xx, yy = x, y
        while True:
            xx, yy = xx + d['x'], yy + d['y']
            if not (0 <= xx < w and 0 <= yy < h):
                break

            if grid[yy][xx] >= cell:
                is_blocked += 1
                break

    return is_blocked < 4


def highest_scenic_score(grid):
    width = len(grid[0])
    height = len(grid)
    score = 0
    for y in range(height):
        for x in range(width):
            score = max(score, scenic_score(grid, x, y, width, height))
    return score


def scenic_score(grid, x, y, w, h):
    directions = [
        {'x': -1, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 0, 'y': -1},
        {'x': 0, 'y': 1},
    ]

    cell = grid[y][x]
    score = 1
    for d in directions:
        xx, yy = x, y
        distance = 0
        while True:
            xx, yy = xx + d['x'], yy + d['y']
            if not (0 <= xx < w and 0 <= yy < h):
                break

            distance += 1
            if grid[yy][xx] >= cell:
                break

        score *= distance

    return score
