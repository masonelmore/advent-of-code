import unittest

from solutions.year2022.day08 import solve_part1, solve_part2
from tests.util import load_input, gen


def example_input():
    return gen([
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ])


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day08.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 1736
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 268800
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = example_input()
        expected = 21
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = example_input()
        expected = 8
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
