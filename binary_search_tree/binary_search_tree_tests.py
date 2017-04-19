import unittest
from binary_search_tree import BST

class BSTTests(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(8)
        self.bst.insert(12)
        self.bst.insert(15)

    def test_print(self):
        self.bst.inorder_tree_walk(self.bst.root)
        self.assertEqual(0, 0)

    def test_search(self):
        node = self.bst.search(self.bst.root, 4)
        self.assertEqual(node, None)
        node = self.bst.search(self.bst.root, 8)
        self.assertEqual(node.data, 8)

    def test_min(self):
        node = self.bst.min(self.bst.root)
        self.assertEqual(node.data, 5)

    def test_remove(self):
        self.bst.remove(self.bst.search(self.bst.root, 5))
        node = self.bst.min(self.bst.root)
        self.assertEqual(node.data, 8)

if __name__ == "__main__":
    unittest.main()
