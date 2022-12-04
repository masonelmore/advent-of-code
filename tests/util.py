from pathlib import Path


def gen(items):
    for item in items:
        yield item


def get_input_filename(test_file):
    test_filename = Path(test_file).name
    # test_YYYYdayDD.py
    #      ^^^^
    year = test_filename[5:9]

    # test_YYYYdayDD.py
    #             ^^
    day = test_filename[12:14]

    input_filename = f'../year{year}/day{day}.txt'
    return input_filename


def load_input(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
