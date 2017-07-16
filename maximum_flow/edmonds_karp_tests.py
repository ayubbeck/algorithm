import unittest
from edmonds_karp import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        source = 's'
        sink = 't'
        vertices = ['s', 'a', 'b', 'c', 'd', 't']
        edges = {
            's': [['a', 4], ['c', 3]],
            'a': [['b', 4]],
            'b': [['t', 2], ['c', 3]],
            'c': [['d', 6]],
            'd': [['t', 6]],
            't': [['t', 0]]
        }
        # vertices = ['s', 'u', 'v', 't']
        # edges = {
        #     's': [['u', 100], ['v', 100]],
        #     'u': [['t', 100], ['v', 1]],
        #     'v': [['t', 100]],
        #     't': [['t', 0]]
        # }
        self.g = Graph(vertices, edges, source, sink)

    def test_flow(self):
        self.assertEqual(self.g.flow, 7)

if __name__ == '__main__':
    unittest.main()
