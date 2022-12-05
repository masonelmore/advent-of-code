import importlib
import string

from pathlib import Path


class Solution:
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def script_filename(self):
        return f'year{self.year}/day{self.day:02}.py'

    def input_filename(self):
        return f'year{self.year}/day{self.day:02}.txt'

    def test_filename(self):
        return f'tests/test_{self.year}day{self.day:02}.py'

    def module_name(self):
        return f'year{self.year}.day{self.day:02}'


class Creator:
    def __init__(self, solution):
        self.solution = solution

    def save_files(self):
        self._save_solution()
        self._save_input_data()
        self._save_test()

    def _save_solution(self):
        if Path(self.solution.script_filename()).exists():
            return

        with open('templates/solution.tpl') as f:
            solution = f.read()
        with open(self.solution.script_filename(), 'w') as f:
            f.write(solution)

    def _save_input_data(self):
        Path(self.solution.input_filename()).touch()

    def _save_test(self):
        if Path(self.solution.test_filename()).exists():
            return

        with open('templates/test.tpl') as f:
            template = string.Template(f.read())
        test = template.substitute(
            {
                'module_name': self.solution.module_name(),
                'input_filename': self.solution.input_filename(),
            }
        )
        with open(self.solution.test_filename(), 'w') as f:
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
                yield line.strip()
