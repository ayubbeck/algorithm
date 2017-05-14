import unittest
from fibonacci import Fibonacci

class FibTests(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_one(self):
        self.assertEqual(self.fib.calc(1), 1)
        self.assertEqual(self.fib.calc(2), 1)
        self.assertEqual(self.fib.calc(3), 2)
        self.assertEqual(self.fib.calc(4), 3)
        self.assertEqual(self.fib.calc(5), 5)
        self.assertEqual(self.fib.calc(6), 8)

    def test_dp_fib(self):
        self.assertEqual(self.fib.memoized_calc(1), 1)
        self.assertEqual(self.fib.memoized_calc(2), 1)
        self.assertEqual(self.fib.memoized_calc(3), 2)
        self.assertEqual(self.fib.memoized_calc(4), 3)
        self.assertEqual(self.fib.memoized_calc(5), 5)
        self.assertEqual(self.fib.memoized_calc(6), 8)

    def test_buttom_up_calc(self):
        self.assertEqual(self.fib.buttom_up_calc(1), 1)
        self.assertEqual(self.fib.buttom_up_calc(2), 1)
        self.assertEqual(self.fib.buttom_up_calc(3), 2)
        self.assertEqual(self.fib.buttom_up_calc(4), 3)
        self.assertEqual(self.fib.buttom_up_calc(5), 5)
        self.assertEqual(self.fib.buttom_up_calc(6), 8)
        self.assertEqual(self.fib.buttom_up_calc(1000000), 8)

if __name__ == '__main__':
    unittest.main()
