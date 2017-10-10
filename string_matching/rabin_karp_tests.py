import unittest
from rabin_karp import RabinKarp

class RabinKarpTests(unittest.TestCase):
    def setUp(self):
        self.rk_one = RabinKarp('abcabaaba', 'aba')
        self.rk_two = RabinKarp('abccdhabacfhfhf', 'abac')
        self.rk_three = RabinKarp('fabdgdtdf', 'fabdgdtdf')

    def test_one(self):
        self.assertEqual(self.rk_one.process(), 3)

    def test_two(self):
        self.assertEqual(self.rk_two.process(), 6)

    def test_three(self):
        self.assertEqual(self.rk_three.process(), 0)

if __name__ == '__main__':
    unittest.main()
