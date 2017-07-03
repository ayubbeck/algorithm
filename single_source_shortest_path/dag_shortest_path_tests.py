import sys
import unittest
from dag_shortest_path import Graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        vertices = ['r', 's', 't', 'x', 'y', 'z']
        edges = {
            'r': [['s', 5], ['t', 3]],
            's': [['t', 2], ['x', 6]],
            't': [['x', 7], ['y', 4], ['z', 2]],
            'x': [['y', -1], ['z', 1]],
            'y': [['z', -2]],
            'z': []
        }
        children = {
            'r': ['s', 't'],
            's': ['t', 'x'],
            't': ['x', 'y', 'z'],
            'x': ['y', 'z'],
            'y': ['z'],
            'z': []
        }
        self.g = Graph(vertices, edges, children, 's')

    def test_dag(self):
        self.assertEqual(self.g.vertices['r'].d, sys.maxint)
        self.assertEqual(self.g.vertices['s'].d, 0)
        self.assertEqual(self.g.vertices['t'].d, 2)
        self.assertEqual(self.g.vertices['x'].d, 6)
        self.assertEqual(self.g.vertices['y'].d, 5)
        self.assertEqual(self.g.vertices['z'].d, 3)

    def test_shortest_path(self):
        self.assertEqual(self.g.shortest_path(self.g.vertices['z']), ['s', 'x', 'y', 'z'])
        self.assertEqual(self.g.shortest_path(self.g.vertices['t']), ['s', 't'])

if __name__ == '__main__':
    unittest.main()
