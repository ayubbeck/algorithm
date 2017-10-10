import unittest
from automata import SMFA

class SMFATests(unittest.TestCase):
    def setUp(self):
        self.text_one = 'abaabcabc'
        self.text_two = 'abaabc'
        self.pattern = 'abc'
        self.chars = ['a', 'b', 'c']
        self.sma_one = SMFA(self.text_one, self.pattern, self.chars)
        self.sma_two = SMFA(self.text_two, self.pattern, self.chars)

    def test_one(self):
        self.assertEqual(self.sma_one.shifts, [3, 6])
        self.assertEqual(self.sma_two.shifts, [3])

if __name__ == '__main__':
    unittest.main()
