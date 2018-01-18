import unittest
from bm import BM

class BmTests(unittest.TestCase):
    def setUp(self):
        self.a = 8
        self.b = 6
        self.bm = BM()

    def test_get_bit(self):
        self.assertEqual(self.bm.get_bit(self.a, 2), 0)
        self.assertNotEqual(self.bm.get_bit(self.a, 3), 0)

    def test_set_bit(self):
        self.assertEqual(self.bm.set_bit(self.a, 2), 12)

    def test_clear_bit(self):
        self.assertEqual(self.bm.clear_bit(self.b, 1), 4)
        self.assertEqual(self.bm.clear_bit(self.b, 2), 2)

    def test_update_bit(self):
        self.assertEqual(self.bm.update_bit(self.b, 3, True), 14)
        self.assertEqual(self.bm.update_bit(self.b, 3, False), 6)
        self.assertEqual(self.bm.update_bit(self.b, 1, False), 4)
        self.assertEqual(self.bm.update_bit(self.b, 1, True), 6)

if __name__ == "__main__":
    unittest.main()
