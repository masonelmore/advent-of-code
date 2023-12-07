import importlib
import string
from datetime import datetime
from pathlib import Path

import requests
from pytz import timezone, utc


class AdventOfCode:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.cookies['session'] = token

    def puzzle_input(self, year, day):
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        resp = self.session.get(url)
        resp.raise_for_status()
        return resp.text.rstrip('\n')

    @classmethod
    def year(cls):
        eastern_dt = cls._datetime_eastern()
        return eastern_dt.year

    @classmethod
    def day(cls):
        eastern_dt = cls._datetime_eastern()
        return eastern_dt.day

    @classmethod
    def _datetime_eastern(cls):
        # https://adventofcode.com/2022/about#faq_unlocktime
        utc_dt = datetime.now(tz=utc)
        eastern = timezone('US/Eastern')
        eastern_dt = utc_dt.astimezone(eastern)
        return eastern_dt


class Solution:
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def script_filename(self):
        return f'solutions/year{self.year}/day{self.day:02}.py'

    def input_filename(self):
        return f'inputs/year{self.year}/day{self.day:02}.txt'

    def test_filename(self):
        return f'tests/year{self.year}/test_day{self.day:02}.py'

    def module_name(self):
        return f'solutions.year{self.year}.day{self.day:02}'


class Creator:
    def __init__(self, aoc, solution):
        self.aoc = aoc
        self.solution = solution

    def save_files(self):
        self._save_solution()
        self._save_input_data()
        self._save_test()

    def _save_solution(self):
        script_path = Path(self.solution.script_filename())
        if script_path.exists():
            return

        script_path.parent.mkdir(parents=True, exist_ok=True)
        with open('templates/solution.tpl') as f:
            solution = f.read()
        with open(script_path, 'w') as f:
            f.write(solution)

    def _save_input_data(self):
        input_path = Path(self.solution.input_filename())
        if input_path.exists():
            return

        input_data = self.aoc.puzzle_input(self.solution.year, self.solution.day)
        input_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.solution.input_filename(), 'w') as f:
            f.write(input_data)

    def _save_test(self):
        test_path = Path(self.solution.test_filename())
        if test_path.exists():
            return

        with open('templates/test.tpl') as f:
            template = string.Template(f.read())

        test = template.substitute(
            {
                'module_name': self.solution.module_name(),
                'input_filename': self.solution.input_filename(),
            }
        )

        test_path.parent.mkdir(parents=True, exist_ok=True)
        with open(test_path, 'w') as f:
            f.write(test)


class Runner:
    def __init__(self, solution):
        self.solution = solution

    def solve(self, part):
        solve_func = self._solve_func(part)
        input_data = self._load_input()
        answer = solve_func(input_data)
        print(f'{self.solution.year}/day{self.solution.day}part{part}: {answer}')

    def _solve_func(self, part):
        module = importlib.import_module(self.solution.module_name())

        if part == 1:
            return module.solve_part1
        else:
            return module.solve_part2

    def _load_input(self):
        with open(self.solution.input_filename()) as f:
            for line in f:
                yield line.rstrip('\n')
