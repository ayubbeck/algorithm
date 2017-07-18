import unittest
from push_relabel import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        vertices = ['s', 'a', 'b', 'c', 'd', 'e', 't']
        edges = {
            's': [['a', 5], ['b', 10], ['d', 4]],
            'a': [['c', 1], ['t', 3]],
            'b': [['c', 7], ['d', 3], ['e', 7]],
            'c': [['t', 5]],
            'd': [['e', 6]],
            'e': [['t', 4]],
            't': [['t', 0]]
        }
        self.source = 's'
        self.sink = 't'
        self.g = Graph(vertices, edges, self.source, self.sink)

    def test_max_flow(self):
        self.assertEqual(self.g.vertices[self.source].excess, -12)
        self.assertEqual(self.g.vertices[self.sink].excess, 12)

if __name__ == '__main__':
    unittest.main()
