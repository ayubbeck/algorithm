import unittest
from kmp import KnuthMorrisPratt

class KnuthMorrisPrattTests(unittest.TestCase):
    def setUp(self):
        text = 'bbababacaccababaca'
        pattern = 'ababaca'
        self.kmp = KnuthMorrisPratt(text, pattern)

    def test_one(self):
        self.assertEqual(self.kmp.shifts, [2, 11])

if __name__ == '__main__':
    unittest.main()
