import unittest
from bfs import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        vertices = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
        edges = {
            'r': ['s', 'v'],
            's': ['r', 'w'],
            't': ['u', 'w', 'x'],
            'u': ['t', 'x', 'y'],
            'v': ['r'],
            'w': ['s', 't', 'x'],
            'x': ['t', 'u', 'w', 'y'],
            'y': ['u', 'x']
        }
        self.g = Graph(vertices, edges)

    def test_one(self):
        self.assertEqual(0, 0)

    def test_bfs_color(self):
        for i in self.g.vertices:
            self.assertEqual(self.g.vertices[i].color, 'BLACK')

    def test_bfs_distance(self):
        self.assertEqual(self.g.vertices['r'].distance, 1)
        self.assertEqual(self.g.vertices['s'].distance, 0)
        self.assertEqual(self.g.vertices['t'].distance, 2)
        self.assertEqual(self.g.vertices['u'].distance, 3)
        self.assertEqual(self.g.vertices['v'].distance, 2)
        self.assertEqual(self.g.vertices['w'].distance, 1)
        self.assertEqual(self.g.vertices['x'].distance, 2)
        self.assertEqual(self.g.vertices['y'].distance, 3)

    def test_shortest_path(self):
        self.assertEqual(self.g.short_path(self.g.vertices['s'], self.g.vertices['y']), ['s', 'w', 'x', 'y'])

if __name__ == '__main__':
    unittest.main()
