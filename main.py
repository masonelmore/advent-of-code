import argparse
import importlib
import string

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Runner for AoC solutions.')
    parser.add_argument('-y', '--year', dest='year', type=str, required=True)
    parser.add_argument('-d', '--day', dest='day', type=str, required=True, action=PaddingAction)
    parser.add_argument('-p', '--part', dest='part', type=int)
    subparsers = parser.add_subparsers()

    parser_run = subparsers.add_parser('run')
    parser_run.set_defaults(func=run)

    parser_create = subparsers.add_parser('create')
    parser_create.set_defaults(func=create)

    args = parser.parse_args()
    args.func(args)


class PaddingAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string=None):
        padded = f'{int(value):02}'
        setattr(namespace, self.dest, padded)


def run(args):
    year = args.year
    day = args.day
    part = args.part

    input_filename = f'year{year}/day{day}.txt'
    solve_funcs = get_solve_funcs(year, day, part)
    for i, solve_func in enumerate(solve_funcs):
        input_data = load_input(input_filename)
        solution = solve_func(input_data)
        part = part or i + 1
        print(f'{args.year}/d{args.day}p{part}: {solution}')


def get_solve_funcs(year, day, part):
    module = importlib.import_module(f'year{year}.day{day}')

    if not part:
        return [module.solve_part1, module.solve_part2]

    if part == 1:
        return [module.solve_part1]
    else:
        return [module.solve_part2]


def load_input(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()


def create(args):
    year = args.year
    day = args.day

    if Path(f'year{year}/day{day}.py').exists():
        raise Exception(f'solution for {year}/day{day} already exists')

    with open('templates/solution.tpl') as f:
        solution = f.read()
    with open(f'year{year}/day{day}.py', 'w') as f:
        f.write(solution)

    Path(f'year{year}/day{day}.txt').touch()

    with open('templates/test.tpl') as f:
        template = string.Template(f.read())
    test = template.substitute({'year': year, 'day': day})
    with open(f'tests/test_{year}day{day}.py', 'w') as f:
        f.write(test)


if __name__ == '__main__':
    main()
