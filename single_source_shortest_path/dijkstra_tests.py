import unittest
from dijkstra import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        vertices = ['s', 't', 'x', 'y', 'z']
        edges = {
            's': [['t', 10], ['y', 5]],
            't': [['x', 1], ['y', 2]],
            'x': [['z', 4]],
            'y': [['t', 3], ['x', 9], ['z', 2]],
            'z': [['s', 7], ['x', 6]]
        }
        self.g = Graph(vertices, edges, 's')

    def test_dijkstra(self):
        self.assertEqual(self.g.vertices['s'].d, 0)
        self.assertEqual(self.g.vertices['t'].d, 8)
        self.assertEqual(self.g.vertices['x'].d, 9)
        self.assertEqual(self.g.vertices['y'].d, 5)
        self.assertEqual(self.g.vertices['z'].d, 7)

    def test_shortest_path(self):
        self.assertEqual(self.g.short_path, ['s', 'y', 'z', 't', 'x'])

if __name__ == '__main__':
    unittest.main()
