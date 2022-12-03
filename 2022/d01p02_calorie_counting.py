def solve(data):
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
