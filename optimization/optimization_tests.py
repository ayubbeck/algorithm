import unittest
from optimization import Optimization

class OptimizationTests(unittest.TestCase):
    def setUp(self):
        # arr = [[1.0, 1.0, 1.0, 0.0, 0.0, 6.0],
        #        [2.0, 1.0, 0.0, 1.0, 0.0, 8.0],
        #        [-1.0, -3.0, 0.0, 0.0, 1.0, 0.0]]
        arr = [[6.0, 9.0, 1.0, 0.0, 0.0, 600.0],
               [5.0, 4.0, 0.0, 1.0, 0.0, 360.0],
               [-6.0, -8.0, 0.0, 0.0, 1.0, 0.0]]
        num_of_var = 2
        self.s = Optimization(arr, num_of_var)

    def test_simplex(self):
        # self.assertEqual(self.s.profit['var'], [0.0, 6.0])
        # self.assertEqual(self.s.profit['profit'], 18.0)
        self.assertEqual(self.s.profit['var'], [40.0, 40.0])
        self.assertEqual(self.s.profit['profit'], 560.0)

if __name__ == '__main__':
    unittest.main()
