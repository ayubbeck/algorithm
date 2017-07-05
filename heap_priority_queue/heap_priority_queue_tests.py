import unittest
from heap_priority_queue import HeapPriorityQueue

class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def __str__(self):
        return str(self.id) + ' ' + str(self.weight)

    def __cmp__(self, other):
        if self.weight < other.weight:
            return -1
        elif self.weight == other.weight:
            return 0
        else:
            return 1

class HeapPriorityQueueTests(unittest.TestCase):
    def setUp(self):
        arr = [
            ['a', 8],
            ['b', 6],
            ['c', 3],
            ['d', 0],
            ['e', 1],
            ['f', 2],
            ['g', 7]
        ]
        self.heap = HeapPriorityQueue()
        self.nodes = {}
        for key, weight in arr:
            node = Node(key, weight)
            self.nodes[key] = node
            self.heap.push(node)

    def test_peek(self):
        self.assertEqual(self.heap.peek().weight, 0)

    def test_pop(self):
        min_item = self.heap.pop()
        self.assertEqual(min_item.weight, 0)
        self.assertEqual(self.heap.peek().weight, 1)

    def test_push(self):
        self.heap.push(Node('i', -1))
        self.assertEqual(self.heap.peek().weight, -1)

    def test_find_and_heapify(self):
        self.nodes['a'].weight = -5
        self.heap.find_and_heapify(self.nodes['a'])
        self.assertEqual(self.heap.peek().weight, -5)

if __name__ == '__main__':
    unittest.main()
