import unittest
from os_tree import OSTree

class OSTreeTests(unittest.TestCase):
    def setUp(self):
        self.rbt = OSTree()
        self.rbt.add(10)
        self.rbt.add(8)
        self.rbt.add(6)
        self.rbt.add(4)
        self.rbt.add(9)

    def test_add(self):
        print '*' * 20
        print self.rbt.root
        print '=' * 20
        self.rbt.inorder_walk(self.rbt.root)
        print '*' * 20
        self.assertEqual(0, 0)

    def test_search(self):
        node = self.rbt.search(4)
        self.assertEqual(node.data, 4)
        self.assertEqual(node.size, 1)

    def test_select(self):
        node = self.rbt.select(self.rbt.root, 4)
        self.assertEqual(node.data, 9)
        self.assertEqual(node.size, 1)

    def test_rank(self):
        node = self.rbt.search(10)
        self.assertEqual(self.rbt.rank(node), 5)

if __name__ == "__main__":
    unittest.main()
