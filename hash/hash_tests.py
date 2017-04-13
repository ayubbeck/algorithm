import unittest
from hash import Hash

class HashTests(unittest.TestCase):
    def setUp(self):
        self.hash = Hash()
        self.hash[0] = 0
        self.hash[1] = 1
        self.hash[2] = 2

    def test_one(self):
        self.assertEqual(self.hash[0], 0)

    def test_two(self):
        self.assertEqual(self.hash[1], 1)

    def test_three(self):
        self.assertEqual(self.hash.get_size(), 12)

if __name__ == '__main__':
    unittest.main()
