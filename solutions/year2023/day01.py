def solve_part1(data):
    return sum(calibration_values(data))


def solve_part2(data):
    return -1


def calibration_values(data, parse_words=False):
    for line in data:
        first_digit = find_digit(line)
        last_digit = find_digit(line[::-1])
        yield int(first_digit + last_digit)


def find_digit(string):
    for char in string:
        if char.isdigit():
            return char
