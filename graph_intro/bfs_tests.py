import unittest
from bfs import BFS, LinkedList

class BFSTests(unittest.TestCase):
    def setUp(self):
        self.bfs = BFS()
        v = [[5, 2, 1], [4, 3, 5, 1, 2], [4, 2, 3], [3, 5, 2, 4], [2, 1, 4, 5]]

        for i in v:
            l = LinkedList()
            for j in i:
                l.add(j)
            self.bfs.adj.append(l)
        self.bfs.bfs(0)

    def test_bfs(self):
        for i in range(len(self.bfs.adj)):
            self.assertEqual(self.bfs.adj[i].head.key, i + 1)
            self.assertEqual(self.bfs.adj[i].head.color, 'BLACK')

    def test_path(self):
        self.assertEqual(self.bfs.short_path(self.bfs.adj[0].head, self.bfs.adj[2].head), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
