import unittest
from lcs import Lcs

class LcsTests(unittest.TestCase):
    def setUp(self):
        self.x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
        self.y = ['B', 'D', 'C', 'A', 'B', 'A']
        self.lcs = Lcs(self.x, self.y)

    def test_one(self):
        # self.lcs.print_it()
        self.assertEqual(0, 0)

    def test_two(self):
        # self.lcs.length()
        # self.lcs.print_it()
        self.assertEqual(0, 0)

    def test_three(self):
        c, b = self.lcs.length()
        self.lcs.print_it()
        print '*' * 20
        self.lcs.print_lines()
        print '*' * 20
        self.lcs.print_lcs(b, self.x, len(self.x), len(self.y))
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
