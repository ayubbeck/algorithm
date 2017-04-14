import unittest
from hash import Hash

class HashTests(unittest.TestCase):
    def setUp(self):
        self.hash = Hash()
        self.hash.add(0)
        self.hash.add(1)
        self.hash.add(2)
        self.hash.add('b')
        self.hash.add('a')

    def test_one(self):
        self.assertEqual(self.hash.get(0), 0)

    def test_two(self):
        self.assertEqual(self.hash.get('a'), 'a')

    def test_three(self):
        self.assertEqual(self.hash.get_size(), 11)

    def test_four(self):
        self.hash.remove('b')
        self.assertEqual(self.hash.get('b'), None)

if __name__ == '__main__':
    unittest.main()
