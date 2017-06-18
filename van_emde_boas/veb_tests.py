import unittest
from veb import VEB

class VEBTests(unittest.TestCase):
    def setUp(self):
        self.veb = VEB(16)
        self.veb.insert(3)
        self.veb.insert(9)

    def test_contains(self):
        self.assertEqual(self.veb.member(3), True)
        self.assertEqual(self.veb.member(5), False)
        self.assertEqual(self.veb.member(9), True)

    def test_successor(self):
        self.assertEqual(self.veb.successor(3), 9)
        self.assertEqual(self.veb.successor(9), None)
        self.assertEqual(self.veb.successor(1), 3)

if __name__ == "__main__":
    unittest.main()
