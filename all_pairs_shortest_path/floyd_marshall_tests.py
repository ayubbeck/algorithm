import unittest
from floyd_warshall import Graph

class FloydWarshallTests(unittest.TestCase):
    def setUp(self):
        vertices = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        edges = {
            'a': [['b', 3], ['c', 8], ['e', -4]],
            'b': [['d', 1], ['e', 7]],
            'c': [['b', 4]],
            'd': [['a', 2], ['c', -5]],
            'e': [['d', 6]]
        }
        self.g = Graph(vertices, edges)

    def test_graph(self):
        self.assertEqual(self.g.dist[self.g.vertices['e']][self.g.vertices['a']], 8)
        self.assertEqual(self.g.next[self.g.vertices['e']][self.g.vertices['a']], 'd')

    def test_path(self):
        self.assertEqual(self.g.shortest_path('a', 'b'), ['a', 'e', 'd', 'c', 'b'])
        self.assertEqual(self.g.shortest_path('d', 'e'), ['d', 'a', 'e'])

if __name__ == '__main__':
    unittest.main()
