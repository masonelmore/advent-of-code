import unittest

from tests.util import load_input, gen
from solutions.year2022.day05 import (
    solve_part1,
    solve_part2,
    get_stacks,
    get_moves,
    move_crates,
    crates_at_top,
    get_stack_locations,
)


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day05.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 'FZCMJCRHZ'
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 'JSDHQMZGF'
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_sample(self):
        input_data = gen([
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 ',
            '',
            'move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2',
        ])

        expected = 'CMZ'
        actual = solve_part1(input_data)
        self.assertEqual(expected, actual)

    def test_part2_sample(self):
        input_data = gen([
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 ',
            '',
            'move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2',
        ])

        expected = 'MCD'
        actual = solve_part2(input_data)
        self.assertEqual(expected, actual)

    def test_get_stacks(self):
        input_data = gen([
            '        [F]',
            '    [D] [E]',
            '[A] [B] [C]',
            ' 1   2   3 ',
            '           ',
            'move 1 from 3 to 1',
        ])

        expected = {
            '1': ['A'],
            '2': ['B', 'D'],
            '3': ['C', 'E', 'F'],
        }

        actual = get_stacks(input_data)
        self.assertEqual(expected, actual)

    def test_get_stack_locations(self):
        locations_line = ' 1   2   3 '
        expected = {
            '1': 1,
            '2': 5,
            '3': 9,
        }
        actual = get_stack_locations(locations_line)
        self.assertEqual(expected, actual)

    def test_get_moves(self):
        input_data = gen([
            'move 1 from 2 to 3',
            'move 10 from 20 to 30',
        ])

        expected = [
            (1, '2', '3'),
            (10, '20', '30'),
        ]

        actual = list(get_moves(input_data))
        self.assertEqual(expected, actual)

    def test_move_crates(self):
        stacks = {
            '1': ['A'],
            '2': ['B'],
            '3': ['C'],
        }

        qty, src, dst = 1, '3', '2'
        expected = {
            '1': ['A'],
            '2': ['B', 'C'],
            '3': [],
        }
        move_crates(stacks, qty, src, dst)
        self.assertEqual(expected, stacks)

        qty, src, dst = 2, '2', '1'
        expected = {
            '1': ['A', 'C', 'B'],
            '2': [],
            '3': [],
        }
        move_crates(stacks, qty, src, dst)
        self.assertEqual(expected, stacks)

    def test_move_multiple_crates(self):
        stacks = {
            '1': ['A'],
            '2': ['B'],
            '3': ['C'],
        }

        qty, src, dst = 1, '3', '2'
        expected = {
            '1': ['A'],
            '2': ['B', 'C'],
            '3': [],
        }
        move_crates(stacks, qty, src, dst, keep_order=True)
        self.assertEqual(expected, stacks)

        qty, src, dst = 2, '2', '1'
        expected = {
            '1': ['A', 'B', 'C'],
            '2': [],
            '3': [],
        }
        move_crates(stacks, qty, src, dst, keep_order=True)
        self.assertEqual(expected, stacks)

    def test_crates_at_top(self):
        stacks = {
            '1': ['A'],
            '2': ['B', 'D'],
            '3': [],
            '4': ['C', 'E', 'F'],
        }

        expected = 'ADF'
        actual = crates_at_top(stacks)
        self.assertEqual(expected, actual)
