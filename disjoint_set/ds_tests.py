import unittest
from ds import DisjointSet, Node

class DisjointSetTests(unittest.TestCase):
    def setUp(self):
        self.ds = DisjointSet(['a', 'b', 'c', 'd', 'e', 'f'])
        self.ds.connected_components()

    def test_key(self):
        self.assertEqual(self.ds.sets[0].key, 'a')

    def test_find_set(self):
        parent = self.ds.find_set(self.ds.sets[5])
        self.assertEqual(parent.key, 'b')

if __name__ == "__main__":
    unittest.main()
