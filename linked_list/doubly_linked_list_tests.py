import unittest
from doubly_linked_list import DoublyLinkedList

class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.items = [1, 2, 3]
        self.l = DoublyLinkedList()

        for i in self.items:
            self.l.add(i)

    def test_find(self):
        for i in self.items:
            node = self.l.find(i)
            key = node.key if node else None
            self.assertEqual(key, i)

    def test_find_and_remove(self):
        self.l.find_and_remove(1)
        self.assertEqual(self.l.peek(self.l.head.right, []), [2, 3])
        self.l.find_and_remove(2)
        self.assertEqual(self.l.peek(self.l.head.right, []), [3])

    def test_peek(self):
        self.assertEqual(self.l.peek(self.l.head.right, []), self.items)

if __name__ == '__main__':
    unittest.main()
