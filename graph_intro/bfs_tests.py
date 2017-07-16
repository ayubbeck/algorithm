import unittest
from bfs import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        source = 's'
        vertices = ['s', 'a', 'b', 'c', 'd', 't']
        edges = {
            'a': ['b'],
            'c': ['d'],
            'b': ['t', 'c'],
            'd': ['t'],
            's': ['a', 'c'],
            't': ['t']
        }
        self.g = Graph(vertices, edges, source)

    def test_bfs_color(self):
        for i in self.g.vertices:
            self.assertEqual(self.g.vertices[i].color, 'BLACK')

    def test_bfs_distance(self):
        self.assertEqual(self.g.vertices['a'].distance, 1)
        self.assertEqual(self.g.vertices['c'].distance, 1)
        self.assertEqual(self.g.vertices['b'].distance, 2)
        self.assertEqual(self.g.vertices['d'].distance, 2)
        self.assertEqual(self.g.vertices['s'].distance, 0)
        self.assertEqual(self.g.vertices['t'].distance, 3)

    def test_shortest_path(self):
        self.assertEqual(self.g.short_path(self.g.vertices['s'], self.g.vertices['t']), ['s', 'a', 'b', 't'])

    def test_invalid_path(self):
        self.assertEqual(self.g.short_path(self.g.vertices['t'], self.g.vertices['s']), [])

    def test_get_path(self):
        self.assertEqual(self.g.get_path(self.g.vertices['s'], self.g.vertices['t']), ['s-a', 'a-b', 'b-t'])

if __name__ == '__main__':
    unittest.main()
