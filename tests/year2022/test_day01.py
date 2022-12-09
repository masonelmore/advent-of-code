import unittest

from solutions.year2022.day01 import solve_part1, solve_part2
from tests.util import load_input


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day01.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 71300
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 209691
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
