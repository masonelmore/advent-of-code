import unittest

from solutions.year2022.day09 import solve_part1, solve_part2, follow
from tests.util import load_input, gen


def example_input1():
    return gen([
        'R 4',
        'U 4',
        'L 3',
        'D 1',
        'R 4',
        'D 1',
        'L 5',
        'R 2',
    ])


def example_input2():
    return gen([
        'R 5',
        'U 8',
        'L 8',
        'D 3',
        'R 17',
        'D 10',
        'L 25',
        'U 20',
    ])


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day09.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 6642
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 2765
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = example_input1()
        expected = 13
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = example_input2()
        expected = 36
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_follow(self):
        test_cases = [
            # ...      ...
            # T.H  ->  .TH
            # ...      ...
            {
                'name': 'right',
                'head': {'x': 2, 'y': 1},
                'tail': {'x': 0, 'y': 1},
                'expected': {'x': 1, 'y': 1},
            },
            # ...      ...
            # H.T  ->  HT.
            # ...      ...
            {
                'name': 'left',
                'head': {'x': 0, 'y': 1},
                'tail': {'x': 1, 'y': 1},
                'expected': {'x': 1, 'y': 1},
            },
            # .H.      .H.
            # ...  ->  .T.
            # .T.      ...
            {
                'name': 'up',
                'head': {'x': 1, 'y': 0},
                'tail': {'x': 1, 'y': 2},
                'expected': {'x': 1, 'y': 1},
            },
            # .T.      ...
            # ...  ->  .T.
            # .H.      .H.
            {
                'name': 'down',
                'head': {'x': 1, 'y': 2},
                'tail': {'x': 1, 'y': 0},
                'expected': {'x': 1, 'y': 1},
            },
            # ..H      ..H
            # ...  ->  ..T
            # .T.      ...
            {
                'name': 'half-diagonal',
                'head': {'x': 2, 'y': 0},
                'tail': {'x': 1, 'y': 2},
                'expected': {'x': 2, 'y': 1},
            },
            # ..H      ..H
            # ...  ->  .T.
            # T..      ...
            {
                'name': 'diagonal',
                'head': {'x': 2, 'y': 0},
                'tail': {'x': 0, 'y': 2},
                'expected': {'x': 1, 'y': 1},
            },
        ]

        for tc in test_cases:
            with self.subTest(tc['name']):
                follow(tc['tail'], tc['head'])
                self.assertEqual(tc['expected'], tc['tail'])
