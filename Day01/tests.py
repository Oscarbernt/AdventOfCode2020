import unittest
from part1 import find_2020 as part1_find_2020
from part2 import find_2020 as part2_find_2020

class TestMethods(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(part1_find_2020("exampleInput.txt"), 514579)

    def test_part2(self):
        self.assertEqual(part2_find_2020("exampleInput.txt"), 241861950)

if __name__ == '__main__':
    unittest.main()