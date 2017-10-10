import unittest
from euclid_gcd import Gcd

class GcdTests(unittest.TestCase):
    def setUp(self):
        a = 500
        b = 150
        self.gcd = Gcd(a, b)

    def test_gcd(self):
        print self.gcd.gcd
        self.assertEqual(0, 0)

    def test_gcd_extended(self):
        print self.gcd.gcd_extended
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
