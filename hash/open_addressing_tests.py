import unittest
from open_addressing import Hash

class HashTests(unittest.TestCase):
    def setUp(self):
        self.hash = Hash()
        self.hash.insert(29)
        self.hash.insert(24)
        self.hash.insert(19)
        self.hash.insert(13)
        self.hash.insert(10)
        print self.hash.table

    def test_one(self):
        self.assertEqual(self.hash.does_key_exist(29), True)

    def test_two(self):
        self.hash.remove(29)
        self.assertEqual(self.hash.does_key_exist(29), False)

    def test_three(self):
        self.assertEqual(self.hash.does_key_exist(15), False)

    def test_four(self):
        self.hash.remove(29)
        self.hash.remove(24)
        self.hash.remove(19)
        self.hash.insert(15)
        self.assertEqual(self.hash.does_key_exist(15), True)

if __name__ == "__main__":
    unittest.main()
