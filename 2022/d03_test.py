import unittest

from d03p01_rucksack_reorganization import item_priority


class TestDay03(unittest.TestCase):

    def test_priorities(self):
        self.assertEqual(item_priority('a'), 1)
        self.assertEqual(item_priority('z'), 26)
        self.assertEqual(item_priority('A'), 27)
        self.assertEqual(item_priority('Z'), 52)
