import unittest

from solutions.year2022.day07 import solve_part1, solve_part2
from tests.util import load_input


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day07.txt'
    example_input = 'testdata/day07.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 1648397
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 1815525
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = load_input(self.example_input)
        expected = 95437
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = load_input(self.example_input)
        expected = 24933642
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
