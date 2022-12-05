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
    def year(arg):
        y = int(arg)
        if y < 2015 or y > 2022:
            raise ValueError
        return y

    def day(arg):
        d = int(arg)
        if d < 1 or d > 25:
            raise ValueError
        return d

    def part(arg):
        p = int(arg)
        if p < 1 or p > 2:
            raise ValueError
        return p

    parser = argparse.ArgumentParser(description='Runner for AoC solutions.')
    parser.add_argument('-y', '--year', dest='year', type=year, required=True)
    parser.add_argument('-d', '--day', dest='day', type=day, required=True)
    parser.add_argument('-p', '--part', dest='part', type=part)
    subparsers = parser.add_subparsers()

    parser_run = subparsers.add_parser('run')
    parser_run.set_defaults(func=run)

    parser_create = subparsers.add_parser('create')
    parser_create.set_defaults(func=create)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
