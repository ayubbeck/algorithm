import unittest
from kruskal import Kruskal

class DisjointSetTests(unittest.TestCase):
    def setUp(self):
        graph = {
            'a': [{'b': 4}, {'h': 8}],
            'b': [{'c': 8}, {'h': 11}],
            'c': [{'d': 7}, {'f': 4}, {'i': 2}],
            'd': [{'e': 9}, {'f': 14}],
            'e': [{'f': 10}],
            'f': [{'g': 2}],
            'g': [{'i': 6}, {'h': 1}],
            'h': [{'i': 7}],
            'i': []
        }
        self.k = Kruskal(graph)

    def test_kruskal(self):
        self.assertEqual(self.k.min_path[0].weight, 1)
        self.assertEqual(self.k.min_path[0].a.key, 'g')
        self.assertEqual(self.k.min_path[0].b.key, 'h')

if __name__ == "__main__":
    unittest.main()
