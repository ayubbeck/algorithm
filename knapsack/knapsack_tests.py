import unittest
from knapsack import Knapsack

class KnapsackTests(unittest.TestCase):
    def setUp(self):
        capacity = 5
        weights = [0, 3, 2, 1]
        values = [0, 5, 3, 4]

        self.knapsack = Knapsack(capacity, weights, values)

    def test_fill(self):
        self.knapsack.fill()
        items = self.knapsack.get_items()
        self.assertEqual(items[0], 3)
        self.assertEqual(items[1], 1)

if __name__ == "__main__":
    unittest.main()
