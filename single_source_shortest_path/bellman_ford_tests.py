import unittest
from bellman_ford import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        vertices = ['s', 't', 'y', 'x', 'z']
        edges = [
            ['s', 't', 6],
            ['s', 'y', 7],
            ['t', 'x', 5],
            ['t', 'y', 8],
            ['t', 'z', -4],
            ['y', 'x', -3],
            ['y', 'z', 9],
            ['x', 't', -2],
            ['z', 'x', 7],
            ['z', 's', 2]
        ]
        self.graph = Graph(vertices, edges, vertices[0])

    def test_bellman_ford(self):
        self.assertEqual(self.graph.bellman_ford(), True)

    def test_shortest_path(self):
        self.graph.bellman_ford()
        self.assertEqual(self.graph.shortest_path(self.graph.vertices['z']), ['s', 'y', 'x', 't', 'z'])

if __name__ == '__main__':
    unittest.main()
