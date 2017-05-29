import unittest
from huffman_code import HuffmanCode, Prioritize

class HuffmanCodeTests(unittest.TestCase):
    def setUp(self):
        self.text = 'applepie'
        self.prioritized = Prioritize(self.text)

    def test_huffman_code(self):
        hc = HuffmanCode(self.prioritized.q, self.prioritized.size)
        root = hc.generate_tree()
        hc.generate_code(root, '')

        self.assertEqual(hc.encode(self.text), '100111100011110101')

if __name__ == "__main__":
    unittest.main()
