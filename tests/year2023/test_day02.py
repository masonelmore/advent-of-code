import unittest

from solutions.year2023.day02 import solve_part1, solve_part2
from tests.util import load_input, gen


def example_input():
    return gen([
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ])


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2023/day02.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 2632
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 69629
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = example_input()
        expected = 8
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = example_input()
        expected = 2286
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
