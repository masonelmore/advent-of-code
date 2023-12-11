import unittest

from solutions.year2023.day03 import solve_part1, solve_part2, Schematic
from tests.util import load_input, gen


def example_input():
    return gen([
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ])


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2023/day03.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 525119
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 0
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = example_input()
        expected = 4361
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = example_input()
        expected = 0
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part_numbers(self):
        data = [
            '1.2',
            '3$4',
            '5.6',
        ]
        expected = [1, 2, 3, 4, 5, 6]
        schematic = Schematic.load(gen(data))
        result = list(schematic.part_numbers())
        self.assertListEqual(expected, result)
