import unittest
from dfs import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        vertices = ['u', 'v', 'w', 'x', 'y', 'z']
        edges = {
            'u': ['v', 'x'],
            'v': ['y'],
            'w': ['y', 'z'],
            'x': ['v'],
            'y': ['x'],
            'z': ['z']
        }
        self.g = Graph(vertices, edges)

    def test_bfs_color(self):
        for i in self.g.vertices:
            self.assertEqual(self.g.vertices[i].color, 'BLACK')

    def test_bfs_distance(self):
        self.assertEqual(self.g.vertices['x'].distance, 4)
        self.assertEqual(self.g.vertices['z'].distance, 10)

    def test_bfs_finish(self):
        self.assertEqual(self.g.vertices['x'].finish, 5)
        self.assertEqual(self.g.vertices['z'].finish, 11)

    def test_topological_sort(self):
        self.assertEqual(self.g.topological_sort(), 'wzuvyx')

if __name__ == '__main__':
    unittest.main()
