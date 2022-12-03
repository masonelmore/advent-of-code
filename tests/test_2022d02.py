import unittest

from util import get_input_filename, load_input
from year2022.d02p01_rock_paper_scissors import solve as solve_p01
from year2022.d02p02_rock_paper_scissors import solve as solve_p02


class TestSolution(unittest.TestCase):

    input_filename = get_input_filename(__file__)

    def test_p01_full(self):
        data = load_input(self.input_filename)
        expected = 12679
        answer = solve_p01(data)
        self.assertEqual(expected, answer)

    def test_p02_full(self):
        data = load_input(self.input_filename)
        expected = 14470
        answer = solve_p02(data)
        self.assertEqual(expected, answer)
