import argparse
import importlib

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Runner for AoC solutions.')
    parser.add_argument('-y', '--year', dest='year', type=str)
    parser.add_argument('-d', '--day', dest='day', type=str, action=PaddingAction)
    parser.add_argument('-p', '--part', dest='part', type=int)
    args = parser.parse_args()

    input_filename = f'year{args.year}/d{args.day}_input.txt'
    solve_funcs = get_solve_funcs(args.year, args.day, args.part)
    for i, solve_func in enumerate(solve_funcs):
        input_data = load_input(input_filename)
        solution = solve_func(input_data)
        part = args.part or i + 1
        print(f'{args.year}/d{args.day}p{part}: {solution}')


class PaddingAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string=None):
        padded = f'{int(value):02}'
        setattr(namespace, self.dest, padded)


def get_solve_funcs(year, day, part):
    filename = find_solution_file(year, day)
    module = importlib.import_module(f'year{year}.{filename}')

    if not part:
        return [module.solve_part1, module.solve_part2]

    if part == 1:
        return [module.solve_part1]
    else:
        return [module.solve_part2]


def find_solution_file(year, day):
    file_pattern = f'year{year}/d{day}_*.py'
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
