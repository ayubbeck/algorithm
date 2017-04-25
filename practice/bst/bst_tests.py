import unittest
from bst import BST

class BSTTests(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.insert(10)
        self.bst.insert(6)
        self.bst.insert(15)
        self.bst.insert(1)
        self.bst.insert(20)

    def test_inorder_walk(self):
        self.bst.inorder_walk(self.bst.root)
        self.assertEqual(0, 0)

    def test_preorder_walk(self):
        print '*'*20
        self.bst.preorder_walk(self.bst.root)
        print '*'*20
        self.assertEqual(0, 0)

    def test_min(self):
        min = self.bst.min(self.bst.root)
        self.assertEqual(min.data, 1)

    def test_search(self):
        node = self.bst.search(20)
        self.assertEqual(node.data, 20)

    def test_remove(self):
        node = self.bst.search(10)
        self.bst.inorder_walk(self.bst.root)
        self.bst.remove(node)
        self.bst.inorder_walk(self.bst.root)
        node = self.bst.search(10)
        self.assertEqual(node, None)

if __name__ == '__main__':
    unittest.main()
