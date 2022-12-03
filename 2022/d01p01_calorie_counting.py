def solve(data):
    max_calories = 0
    for calories in calorie_counts(data):
        if calories > max_calories:
            max_calories = calories
    return max_calories


def calorie_counts(data):
    calories = 0
    for item in data:
        if not item:
            yield calories
            calories = 0
            continue
        calories += int(item)
    yield calories
