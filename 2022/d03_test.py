import unittest

from d03p01_rucksack_reorganization import item_priority
from d03p02_rucksack_reorganization import rucksack_groups
from d03p02_rucksack_reorganization import solve as solve_p02


class TestDay03(unittest.TestCase):

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
            actual = list(rucksack_groups(test_case['rucksacks']))
            self.assertEqual(actual, test_case['expected'])

    def test_solution_p02(self):
        expected = item_priority('c')
        self.assertEqual(solve_p02(['abc', 'bcd', 'cde']), expected)
        self.assertEqual(solve_p02(['ccc', 'bcd', 'cde']), expected)
