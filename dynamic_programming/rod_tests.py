import unittest
from rod import Rod

class RodTests(unittest.TestCase):
    def setUp(self):
        price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.rod = Rod(price)

    def test_cut(self):
        # self.assertEqual(self.rod.cut(20), 60)
        pass

    def test_memoized_cut(self):
        self.assertEqual(self.rod.memoized_cut(20), 60)

    def test_buttom_up_cut(self):
        self.assertEqual(self.rod.bottom_up_cut(20), 60)

if __name__ == '__main__':
    unittest.main()
