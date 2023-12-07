import unittest

from solutions.year2022.day11 import solve_part1, solve_part2
from tests.util import load_input


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day11.txt'
    example_input = 'testdata/day11.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 50830
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 0
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = load_input(self.example_input)
        expected = 10605
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = load_input(self.example_input)
        expected = 2713310158
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
