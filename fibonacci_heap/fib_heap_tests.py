import unittest
from fib_heap import FibHeap

class FibHeapTests(unittest.TestCase):
    def setUp(self):
        self.fib_heap = FibHeap()
        self.fib_heap.insert(20)
        self.fib_heap.insert(10)
        self.fib_heap.insert(5)

    def test_peek(self):
        print '.' * 20
        self.fib_heap.root_list.display()
        print '.' * 20
        self.assertEqual(self.fib_heap.peek(), 5)

    def test_extract_min(self):
        min_key = self.fib_heap.extract_min()
        if min_key is not None:
            min_key = min_key.key
        print '&' * 20
        print 'min_key: ', min_key
        print 'next min_key: ', self.fib_heap.peek()
        self.fib_heap.root_list.display()
        print '&' * 20
        self.assertEqual(min_key, 5)

        min_key = self.fib_heap.extract_min()
        if min_key is not None:
            min_key = min_key.key
        print '&' * 20
        print 'min_key: ', min_key
        print 'next min_key: ', self.fib_heap.peek()
        self.fib_heap.root_list.display()
        print '&' * 20
        self.assertEqual(min_key, 10)

        min_key = self.fib_heap.extract_min()
        if min_key is not None:
            min_key = min_key.key
        print '&' * 20
        print 'min_key: ', min_key
        print 'next min_key: ', self.fib_heap.peek()
        self.fib_heap.root_list.display()
        print '&' * 20
        self.assertEqual(min_key, 20)

        min_key = self.fib_heap.extract_min()
        if min_key is not None:
            min_key = min_key.key
        print '&' * 20
        print 'min_key: ', min_key
        print 'next min_key: ', self.fib_heap.peek()
        self.fib_heap.root_list.display()
        print '&' * 20
        self.assertEqual(min_key, None)

if __name__ == '__main__':
    unittest.main()
