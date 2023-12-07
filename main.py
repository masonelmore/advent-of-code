import argparse
import os
from pathlib import Path

from aoc import Solution, Creator, Runner, AdventOfCode


def main():
    args = parse_args()
    args.func(args)


def run(args):
    solution = Solution(args.year, args.day)
    runner = Runner(solution)

    if not args.part:
        parts = [1, 2]
    else:
        parts = [args.part]

    for part in parts:
        runner.solve(part)


def create(args):
    token = load_token()
    if not token:
        print('Token must be set in AOC_TOKEN or ~/.config/aoc/token')
        exit(1)
    aoc = AdventOfCode(token=token)
    solution = Solution(args.year, args.day)
    creator = Creator(aoc, solution)
    creator.save_files()


def load_token():
    token = os.getenv('AOC_TOKEN')
    if token:
        return token

    token_path = Path(os.path.expanduser('~/.config/aoc/token'))
    if token_path.exists():
        with open(token_path) as f:
            token = f.read().strip()
        return token

    return None


def parse_args():
    def validate_int_range(arg, value, start, end):
        i = int(value)
        if i < start or i > end:
            msg = f'{arg} must be between {start} and {end}'
            raise argparse.ArgumentTypeError(msg)
        return i

    def year(arg):
        return validate_int_range(arg='year', value=arg, start=2015, end=2023)

    def day(arg):
        return validate_int_range(arg='day', value=arg, start=1, end=25)

    def part(arg):
        return validate_int_range(arg='part', value=arg, start=1, end=2)

    parser = argparse.ArgumentParser(description='Runner for AoC solutions.')
    parser.add_argument('-y', '--year', dest='year', type=year)
    parser.add_argument('-d', '--day', dest='day', type=day)
    parser.add_argument('-p', '--part', dest='part', type=part)
    subparsers = parser.add_subparsers()

    parser_run = subparsers.add_parser('run')
    parser_run.set_defaults(func=run)

    parser_create = subparsers.add_parser('create')
    parser_create.set_defaults(func=create)

    args = parser.parse_args()

    if not args.year:
        args.year = AdventOfCode.year()

    if not args.day:
        args.day = AdventOfCode.day()

    return args


if __name__ == '__main__':
    main()
