import unittest

from util import load_input
from year2022.day02 import solve_part1, solve_part2


class TestSolution(unittest.TestCase):

    input_filename = '../year2022/day02.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 12679
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 14470
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
