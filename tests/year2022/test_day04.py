import unittest

from tests.util import load_input, gen
from solutions.year2022.day04 import (
    solve_part1,
    solve_part2,
    section_ids,
    section_assignments,
    full_overlap,
    partial_overlap,
)


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day04.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 526
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 886
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_section_assignments(self):
        data = gen([
            '1-3,4-6',
            '7-9,8-10',
        ])
        assignments = section_assignments(data)

        a, b = next(assignments)
        self.assertEqual(a, [1, 2, 3])
        self.assertEqual(b, [4, 5, 6])

        a, b = next(assignments)
        self.assertEqual(a, [7, 8, 9])
        self.assertEqual(b, [8, 9, 10])

    def test_section_ids(self):
        self.assertEqual(section_ids('1-1'), [1])
        self.assertEqual(section_ids('10-12'), [10, 11, 12])

    def test_full_overlap(self):
        self.assertEqual(full_overlap([1], [1]), True)
        self.assertEqual(full_overlap([1], [2]), False)
        self.assertEqual(full_overlap([1, 2], [2, 3]), False)
        self.assertEqual(full_overlap([1, 2, 3, 4], [2, 3]), True)

    def test_partial_overlap(self):
        self.assertEqual(partial_overlap([1], [1, 2]), True)
        self.assertEqual(partial_overlap([1], [2]), False)
        self.assertEqual(partial_overlap([1, 2, 3], [2]), True)
