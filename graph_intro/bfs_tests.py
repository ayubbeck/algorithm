import unittest
from bfs import BFS

class BFSTests(unittest.TestCase):
    def setUp(self):
        graph = {
            'r': ['s', 'v'],
            's': ['r', 'w'],
            't': ['u', 'w', 'x'],
            'u': ['t', 'x', 'y'],
            'v': ['r'],
            'w': ['s', 't', 'x'],
            'x': ['t', 'u', 'w', 'y'],
            'y': ['u', 'x']
        }
        self.bfs = BFS(graph)

    def test_bfs_color(self):
        for i in self.bfs.vertices:
            self.assertEqual(self.bfs.vertices[i].color, 'BLACK')

    def test_bfs_distance(self):
        self.assertEqual(self.bfs.vertices['r'].distance, 1)
        self.assertEqual(self.bfs.vertices['s'].distance, 0)
        self.assertEqual(self.bfs.vertices['t'].distance, 2)
        self.assertEqual(self.bfs.vertices['u'].distance, 3)
        self.assertEqual(self.bfs.vertices['v'].distance, 2)
        self.assertEqual(self.bfs.vertices['w'].distance, 1)
        self.assertEqual(self.bfs.vertices['x'].distance, 2)
        self.assertEqual(self.bfs.vertices['y'].distance, 3)

    def test_shortest_path(self):
        self.assertEqual(
            self.bfs.short_path(self.bfs.vertices['s'], self.bfs.vertices['y']),
            ['s', 'w', 'x', 'y']
        )

if __name__ == '__main__':
    unittest.main()
