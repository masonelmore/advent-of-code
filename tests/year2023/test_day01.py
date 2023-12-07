import unittest

from solutions.year2023.day01 import solve_part1, solve_part2
from tests.util import load_input, gen


def example_input1():
    return gen([
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet',
    ])


def example_input2():
    return gen([
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen',
    ])


class TestSolution(unittest.TestCase):
    input_filename = '../../inputs/year2023/day01.txt'

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 54953
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 53868
        answer = solve_part2(data)
        self.assertEqual(expected, answer)

    def test_part1_example(self):
        data = example_input1()
        expected = 142
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_example(self):
        data = example_input2()
        expected = 281
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
