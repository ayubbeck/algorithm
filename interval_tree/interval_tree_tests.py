import unittest
from interval_tree import IntervalTree
from interval_tree import Interval

class IntervalTreeTests(unittest.TestCase):
    def setUp(self):
        self.rbt = IntervalTree()
        self.rbt.add(8, 10)
        self.rbt.add(1, 4)
        self.rbt.add(15, 18)

    def test_add(self):
        print '*' * 20
        print self.rbt.root
        print '=' * 20
        self.rbt.inorder_walk(self.rbt.root)
        print '*' * 20
        self.assertEqual(0, 0)

    def test_search(self):
        interval = Interval(1, 6)
        node = self.rbt.search(interval)
        self.assertEqual(node.interval.low, 1)
        self.assertEqual(node.interval.high, 4)

        interval = Interval(20, 22)
        node = self.rbt.search(interval)
        self.assertEqual(node, self.rbt.dummy)

if __name__ == "__main__":
    unittest.main()
