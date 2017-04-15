import unittest
from linear_probing import Hash

class HashTests(unittest.TestCase):
    def setUp(self):
        self.hash = Hash()
        self.hash.insert(29)
        self.hash.insert(24)
        self.hash.insert(19)
        self.hash.insert(14)

    def test_one(self):
        self.assertEqual(self.hash.does_key_exist(29), True)

    def test_two(self):
        self.hash.remove(29)
        self.assertEqual(self.hash.does_key_exist(29), False)

    def test_three(self):
        self.assertEqual(self.hash.does_key_exist(15), False)

if __name__ == "__main__":
    unittest.main()
