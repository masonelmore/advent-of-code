import unittest

from util import gen, get_input_filename, load_input
from year2022.d03p01_rucksack_reorganization import item_priority
from year2022.d03p02_rucksack_reorganization import rucksack_groups
from year2022.d03p01_rucksack_reorganization import solve as solve_p01
from year2022.d03p02_rucksack_reorganization import solve as solve_p02


class TestSolution(unittest.TestCase):

    input_filename = get_input_filename(__file__)

    def test_p01_full(self):
        data = load_input(self.input_filename)
        expected = 7691
        answer = solve_p01(data)
        self.assertEqual(expected, answer)

    def test_p02_full(self):
        data = load_input(self.input_filename)
        expected = 2508
        answer = solve_p02(data)
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

    def test_p02_simple(self):
        expected = item_priority('c')
        self.assertEqual(solve_p02(gen(['abc', 'bcd', 'cde'])), expected)
        self.assertEqual(solve_p02(gen(['ccc', 'bcd', 'cde'])), expected)
