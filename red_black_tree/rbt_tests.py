import unittest
from rbt import RedBlackTree

class RedBlackTreeTests(unittest.TestCase):
    def setUp(self):
        self.rbt = RedBlackTree()
        self.rbt.add(10)
        self.rbt.add(9)
        self.rbt.add(8)
        self.rbt.add(7)
        self.rbt.add(6)
        self.rbt.add(5)
        self.rbt.add(4)
        self.rbt.add(3)

    def test_add(self):
        print '*' * 20
        print self.rbt.root
        print '=' * 20
        self.rbt.inorder_walk(self.rbt.root)
        print '*' * 20
        self.assertEqual(0, 0)

    def test_search(self):
        node = self.rbt.search(8)
        self.assertEqual(node.data, 8)

    def test_delete(self):
        node = self.rbt.search(8)
        self.rbt.delete(node)
        print '*' * 20
        print self.rbt.root
        print '=' * 20
        self.rbt.inorder_walk(self.rbt.root)
        print '*' * 20
        self.assertEqual(self.rbt.search(8), self.rbt.dummy)

if __name__ == "__main__":
    unittest.main()
