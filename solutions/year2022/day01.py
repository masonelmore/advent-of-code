def solve_part1(data):
    max_calories = 0
    for calories in calorie_counts(data):
        if calories > max_calories:
            max_calories = calories
    return max_calories


def solve_part2(data):
    sorted_calories = sorted(calorie_counts(data), reverse=True)
    return sum(sorted_calories[:3])


def calorie_counts(data):
    calories = 0
    for item in data:
        if not item:
            yield calories
            calories = 0
            continue
        calories += int(item)
    yield calories
