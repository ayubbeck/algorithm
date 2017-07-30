import unittest
from lup_factor import Matrix

class MatrixTests(unittest.TestCase):
    def setUp(self):
        a = [ [2, 1, 3],
              [4, -1, 3],
              [-2, 5, 5] ]
        b = [17, 31, -5]
        self.m = Matrix(a, b)

    def test_y(self):
        self.assertEqual(self.m.y[0], 17)
        self.assertEqual(self.m.y[1], -3)
        self.assertEqual(self.m.y[2], 6)

    def test_x(self):
        self.assertEqual(self.m.x[0], 5)
        self.assertEqual(self.m.x[1], -2)
        self.assertEqual(self.m.x[2], 3)

if __name__ == '__main__':
    unittest.main()
