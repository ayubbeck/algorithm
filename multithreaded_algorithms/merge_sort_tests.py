import unittest
from merge_sort import MergeSort

class MergeSortTests(unittest.TestCase):
    def setUp(self):
        arr = [9, 3, 5, 0, 1, 2]
        self.ms = MergeSort(arr)

    def test_one(self):
        self.assertEqual(self.ms.arr, [0, 1, 2, 3, 5, 9])

if __name__ == '__main__':
    unittest.main()
