import unittest

from solutions.year2022.day10 import solve_part1, solve_part2
from tests.util import load_input


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2022/day10.txt'
    example_input = 'testdata/day10.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 14920
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = [
            '###..#..#..##...##...##..###..#..#.####.',
            '#..#.#..#.#..#.#..#.#..#.#..#.#..#....#.',
            '###..#..#.#....#..#.#....###..#..#...#..',
            '#..#.#..#.#....####.#....#..#.#..#..#...',
            '#..#.#..#.#..#.#..#.#..#.#..#.#..#.#....',
            '###...##...##..#..#..##..###...##..####.',
        ]
        answer = solve_part2(data, draw=False)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = load_input(self.example_input)
        expected = 13140
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = load_input(self.example_input)
        expected = [
            '##..##..##..##..##..##..##..##..##..##..',
            '###...###...###...###...###...###...###.',
            '####....####....####....####....####....',
            '#####.....#####.....#####.....#####.....',
            '######......######......######......####',
            '#######.......#######.......#######.....',
        ]
        answer = solve_part2(data, draw=False)
        self.assertEqual(expected, answer)
