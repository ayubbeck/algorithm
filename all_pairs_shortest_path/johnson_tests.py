import unittest
from johnson import Graph

class JohnsonTests(unittest.TestCase):
    def setUp(self):
        vertices = {'w': 0, 'x': 1, 'y': 2, 'z': 3}
        edges = [
            ['w', 'z', 2],
            ['x', 'w', 6],
            ['x', 'y', 3],
            ['y', 'w', 4],
            ['y', 'z', 5],
            ['z', 'x', -7],
            ['z', 'y', -3]
        ]
        self.graph = Graph(vertices, edges)

    def test_shortest_dist(self):
        self.assertEqual(self.graph.shortest_dist('w', 'w'), 0)
        self.assertEqual(self.graph.shortest_dist('w', 'x'), -5)
        self.assertEqual(self.graph.shortest_dist('w', 'y'), -2)
        self.assertEqual(self.graph.shortest_dist('w', 'z'), 2)
        self.assertEqual(self.graph.shortest_dist('z', 'x'), -7)

    def test_shortest_path(self):
        self.assertEqual(self.graph.shortest_path('w', 'w'), ['w'])
        self.assertEqual(self.graph.shortest_path('w', 'x'), ['w', 'z', 'x'])
        self.assertEqual(self.graph.shortest_path('w', 'y'), ['w', 'z', 'x', 'y'])
        self.assertEqual(self.graph.shortest_path('w', 'z'), ['w', 'z'])
        self.assertEqual(self.graph.shortest_path('y', 'z'), ['y', 'z'])

if __name__ == '__main__':
    unittest.main()
