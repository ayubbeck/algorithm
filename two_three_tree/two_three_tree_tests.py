import unittest
from two_three_tree import TwoThreeTree

class TwoThreeTreeTests(unittest.TestCase):
    def setUp(self):
        lst = [13, 7, 24, 15, 4, 29, 20, 16, 19, 1, 5, 22, 17]

        self.tree = TwoThreeTree()

        # for item in lst:
        self.tree.insert(13)
        self.tree.insert(7)
        self.tree.insert(24)
        self.tree.insert(15)
        self.tree.insert(4)

        self.tree.insert(29)
        self.tree.insert(20)
        self.tree.insert(16)
        self.tree.insert(19)
        self.tree.insert(1)

        self.tree.insert(5)
        self.tree.insert(22)
        self.tree.insert(17)


    def test_one(self):
        hello = self.tree.find(90)
        self.tree.preorder()

        self.assertEqual(self.tree.find(90), False)

if __name__ == "__main__":
    unittest.main()
