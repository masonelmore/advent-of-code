def main():
    input_data = load_input('d01_input.txt')
    solution = solve(input_data)
    print(solution)


def load_input(filename):
    with open(filename) as f:
        return f.readlines()


def solve(data):
    max_calories = 0
    for calories in calorie_counts(data):
        if calories > max_calories:
            max_calories = calories
    return max_calories


def calorie_counts(data):
    calories = 0
    for item in data:
        item = item.strip()
        if not item:
            yield calories
            calories = 0
            continue
        calories += int(item)
    yield calories


if __name__ == '__main__':
    main()
