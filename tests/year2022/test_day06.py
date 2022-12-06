import unittest

from tests.util import load_input
from solutions.year2022.day06 import solve_part1, solve_part2


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day06.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 1578
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 2178
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
