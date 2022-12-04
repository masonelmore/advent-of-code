import unittest

from util import get_input_filename, load_input
from year2022.d01_calorie_counting import solve_part1
from year2022.d01_calorie_counting import solve_part2


class TestSolution(unittest.TestCase):

    input_filename = get_input_filename(__file__)

    def test_part1_full(self):
        data = load_input(self.input_filename)
        expected = 71300
        answer = solve_part1(data)
        self.assertEqual(expected, answer)

    def test_part2_full(self):
        data = load_input(self.input_filename)
        expected = 209691
        answer = solve_part2(data)
        self.assertEqual(expected, answer)
