import unittest
from jarvis import Point, ConvexHull

class ConvexHullTests(unittest.TestCase):
    def setUp(self):
        coords = [[0, 3],
                  [2, 3],
                  [1, 1],
                  [2, 1],
                  [3, 0],
                  [0, 0],
                  [3, 3]]
        points = []
        for coord in coords:
            points.append(Point(coord[0], coord[1]))
        self.convex_full = ConvexHull(points)
        self.convex_full.find()

    def test(self):
        self.assertEqual(self.convex_full.hull[0].x, 0)
        self.assertEqual(self.convex_full.hull[0].y, 3)
        self.assertEqual(self.convex_full.hull[1].x, 0)
        self.assertEqual(self.convex_full.hull[1].y, 0)
        self.assertEqual(self.convex_full.hull[2].x, 3)
        self.assertEqual(self.convex_full.hull[2].y, 0)
        self.assertEqual(self.convex_full.hull[3].x, 3)
        self.assertEqual(self.convex_full.hull[3].y, 3)

if __name__ == '__main__':
    unittest.main()
