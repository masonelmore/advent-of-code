import unittest

from solutions.year2022.day03 import (
    solve_part1,
    solve_part2,
    item_priority,
    rucksack_groups,
)
from tests.util import gen, load_input


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day03.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 7691
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 2508
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_priorities(self):
        self.assertEqual(item_priority('a'), 1)
        self.assertEqual(item_priority('z'), 26)
        self.assertEqual(item_priority('A'), 27)
        self.assertEqual(item_priority('Z'), 52)

    def test_groups(self):
        test_cases = [
            {
                'rucksacks': ['a', 'a', 'a'],
                'expected': [
                    ['a', 'a', 'a'],
                ],
            },
            {
                'rucksacks': ['a', 'a', 'a', 'b', 'b', 'b'],
                'expected': [
                    ['a', 'a', 'a'],
                    ['b', 'b', 'b'],
                ],
            },
        ]

        for test_case in test_cases:
            actual = list(rucksack_groups(gen(test_case['rucksacks'])))
            self.assertEqual(actual, test_case['expected'])

    def test_part2_simple(self):
        expected = item_priority('c')
        self.assertEqual(solve_part2(gen(['abc', 'bcd', 'cde'])), expected)
        self.assertEqual(solve_part2(gen(['ccc', 'bcd', 'cde'])), expected)
