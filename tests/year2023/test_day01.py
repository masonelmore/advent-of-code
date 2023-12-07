import unittest

from solutions.year2023.day01 import solve_part1, solve_part2
from tests.util import load_input, gen


def example_input():
    return gen([
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet',
    ])


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2023/day01.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 54953
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 0
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = example_input()
        expected = 142
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = example_input()
        expected = 0
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
