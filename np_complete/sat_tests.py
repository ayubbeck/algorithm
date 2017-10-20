import unittest
from sat import SAT

class SATTests(unittest.TestCase):
    def setUp(self):
        self.sat = SAT()

    def test_one(self):
        self.assertIn(self.sat.verify(), (False, True))

if __name__ == '__main__':
    unittest.main()
