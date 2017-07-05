import unittest
from singly_linked_list import SinglyLinkedList

class SinglyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.items = [1, 2, 3]
        self.l = SinglyLinkedList()
        for i in self.items:
            self.l.add(i)

    def test_find(self):
        for i in self.items:
            node = self.l.find(i)
            key = node.key if node else None
            self.assertEqual(key, i)

    def test_remove(self):
        self.l.remove(1)
        self.assertEqual(self.l.peek(self.l.head, []), [2, 3])
        self.l.remove(3)
        self.assertEqual(self.l.peek(self.l.head, []), [2])

    def test_content(self):
        self.assertEqual(self.l.peek(self.l.head, []), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
