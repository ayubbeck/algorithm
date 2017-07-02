import unittest
from prim import Prim

class PrimTests(unittest.TestCase):
    def setUp(self):
        graph = {
            'a': [{'b': 4}, {'h': 8}],
            'b': [{'a': 4}, {'c': 8}, {'h': 11}],
            'c': [{'b': 8}, {'d': 7}, {'f': 4}, {'i': 2}],
            'd': [{'c': 7}, {'e': 9}, {'f': 14}],
            'e': [{'d': 9}, {'f': 10}],
            'f': [{'e': 10}, {'d': 14}, {'c': 4}, {'g': 2}],
            'g': [{'f': 2}, {'i': 6}, {'h': 1}],
            'h': [{'a': 8}, {'b': 11}, {'g': 1}, {'i': 7}],
            'i': [{'c': 2}, {'g': 6}, {'h': 7}]
        }
        self.prim = Prim(graph)

    def test_prim(self):
        self.assertEqual(self.prim.min_path[0], 'a->b')
        self.assertEqual(self.prim.min_path[1], 'a->h')
        self.assertEqual(self.prim.min_path[2], 'h->g')
        self.assertEqual(self.prim.min_path[3], 'g->f')
        self.assertEqual(self.prim.min_path[4], 'f->c')
        self.assertEqual(self.prim.min_path[5], 'c->i')
        self.assertEqual(self.prim.min_path[6], 'c->d')
        self.assertEqual(self.prim.min_path[7], 'd->e')

    def test_weight(self):
        self.assertEqual(self.prim.total_weight, 37)

if __name__ == "__main__":
    unittest.main()
