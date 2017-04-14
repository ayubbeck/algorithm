import unittest
from doubly_linked_list import DoublyLinkedList

class DoublyLinkedTests(unittest.TestCase):
    def setUp(self):
        self.l = DoublyLinkedList()
        self.l.add('a')
        self.l.add('b')
        self.l.add('c')

    def test_one(self):
        self.assertEqual(self.l.__str__(), 'c b a')

    def test_two(self):
        self.assertEqual(self.l.search('a').__str__(), 'a' )

    def test_three(self):
        self.assertEqual(self.l.get('a'), 'a')

    def test_four(self):
        self.l.remove_node(self.l.search('b'))
        self.assertEqual(self.l.__str__(), 'c a')

    def test_four(self):
        self.l.remove_data('c')
        self.assertEqual(self.l.__str__(), 'b a')


if __name__ == '__main__':
    unittest.main()
