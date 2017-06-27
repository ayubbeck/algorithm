import unittest
from dfs import DFS, LinkedList, Vertex

class DFSTests(unittest.TestCase):
    def setUp(self):
        graph = {
            'u': ['v', 'x'],
            'v': ['y'],
            'w': ['y', 'z'],
            'x': ['v'],
            'y': ['x'],
            'z': ['z']
        }
        self.dfs = DFS(graph)

    def test_bfs_color(self):
        for i in self.dfs.vertices:
            self.assertEqual(self.dfs.vertices[i].color, 'BLACK')

    def test_bfs_distance(self):
        self.assertEqual(self.dfs.vertices['x'].distance, 2)
        self.assertEqual(self.dfs.vertices['z'].distance, 10)

    def test_bfs_finish(self):
        self.assertEqual(self.dfs.vertices['x'].finish, 7)
        self.assertEqual(self.dfs.vertices['z'].finish, 11)

    def test_topological_sort(self):
        self.assertEqual(self.dfs.topological_sort(), 'wzuxvy')

if __name__ == '__main__':
    unittest.main()
