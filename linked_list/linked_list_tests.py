import unittest
from linked_list import LinkedList

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.items = [1, 2, 3]
        self.l = LinkedList()
        for i in self.items:
            self.l.add(i)

    def test_linked_list(self):
        for i in self.items:
            node = self.l.find(i)
            key = node.key if node else None
            self.assertEqual(key, i)

if __name__ == '__main__':
    unittest.main()
