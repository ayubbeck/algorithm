import unittest
from matrix import Matrix

class MatrixTests(unittest.TestCase):
    def setUp(self):
        arr = [30, 35, 15, 5, 10, 20, 25]
        self.matrix = Matrix(arr)

    def test_chain_order(self):
        m, s = self.matrix.chain_order()
        self.assertEqual(m, 15125)
        self.assertEqual(s, 3)

if __name__ == '__main__':
    unittest.main()
