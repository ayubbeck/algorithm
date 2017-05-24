import unittest
from activity import Activity

class ActivityTests(unittest.TestCase):
    def setUp(self):
        items = [ _ for _ in range(11)]
        start = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
        finish = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
        self.activity = Activity(items, start, finish)

    def test_one(self):
        items = self.activity.selector()
        print items
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
