import argparse
import importlib

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Runner for AoC solutions.')
    parser.add_argument('-y', '--year', dest='year', type=str)
    parser.add_argument('-d', '--day', dest='day', type=str, action=PaddingAction)
    parser.add_argument('-p', '--part', dest='part', type=str, action=PaddingAction)
    args = parser.parse_args()

    solve = get_solve_func(args.year, args.day, args.part)
    input_filename = f'year{args.year}/d{args.day}_input.txt'
    input_data = load_input(input_filename)
    solution = solve(input_data)
    print(f'{args.year}/d{args.day}p{args.part}: {solution}')


class PaddingAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string=None):
        padded = f'{int(value):02}'
        setattr(namespace, self.dest, padded)


def get_solve_func(year, day, part):
    filename = find_solution_file(year, day, part)
    module = importlib.import_module(f'year{year}.{filename}')
    return module.solve


def find_solution_file(year, day, part):
    file_pattern = f'year{year}/d{day}p{part}_*'
    files = list(Path('.').glob(file_pattern))
    if len(files) > 1:
        raise Exception(f'too many files found for "{file_pattern}"', files)
    elif not files:
        raise Exception(f'no files found for "{file_pattern}"')
    else:
        return files[0].stem


def load_input(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


if __name__ == '__main__':
    main()
