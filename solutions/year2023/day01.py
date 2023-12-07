def solve_part1(data):
    return sum(calibration_values(data))


def solve_part2(data):
    return sum(calibration_values(data, parse_words=True))


def calibration_values(data, parse_words=False):
    for line in data:
        first_digit = parse_first_digit(line, parse_words)
        last_digit = parse_last_digit(line, parse_words)
        yield int(first_digit + last_digit)


def find_digit(string):
    for char in string:
        if char.isdigit():
            return char


def parse_first_digit(string, parse_words=False):
    for i, char in enumerate(string):
        if char.isdigit():
            return char

        if not parse_words:
            continue

        digit = parse_word(string[i:])
        if digit:
            return digit


def parse_last_digit(string, parse_words=False):
    for i, char in enumerate(string[::-1]):
        if char.isdigit():
            return char

        if not parse_words:
            continue

        substring = string[len(string)-i-1:]
        digit = parse_word(substring)
        if digit:
            return digit


def parse_word(string):
    words = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
    ]
    for digit, word in enumerate(words):
        if string.startswith(word):
            return str(digit)
