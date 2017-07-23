import unittest
from fib import Fibonacci

class FibonacciTests(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci(10)

    def test_one(self):
        self.assertEqual(self.fib.q.get(), 89)

if __name__ == '__main__':
    unittest.main()
