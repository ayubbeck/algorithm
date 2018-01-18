import unittest
from trie import Trie
class TrieTests(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert('ab')
        self.trie.insert('abs')
        self.trie.insert('a')
        self.trie.insert('an')
        self.trie.insert('any')
        self.trie.insert('anyhow')
        self.trie.insert('all')

    def test_query(self):
        self.assertEqual(self.trie.query('abs'), True)
        self.assertEqual(self.trie.query('all'), True)
        self.assertEqual(self.trie.query('a'), True)
        self.assertEqual(self.trie.query('absolute'), False)

    def test_prefixes(self):
        self.assertEqual(self.trie.prefixes('anyhow'), ['a', 'an', 'any'])
        self.assertEqual(self.trie.prefixes('abs'), ['a', 'ab'])
        self.assertEqual(self.trie.prefixes('all'), ['a'])
        self.assertEqual(self.trie.prefixes('hawk'), [])

if __name__ == '__main__':
    unittest.main()
