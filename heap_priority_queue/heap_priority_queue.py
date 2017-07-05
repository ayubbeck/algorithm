import math

class HeapPriorityQueue:
    def __init__(self, arr=None):
        self.arr = arr if arr else []
        self.size = len(arr) if arr else 0
        self.build_heap()

    def increase_size(self):
        self.size = self.size + 1

    def decrease_size(self):
        self.size = self.size - 1

    def first_index(self):
        return 0

    def last_index(self):
        return self.size - 1

    def left(self, i):
        return (i * 2) + 1

    def right(self, i):
        return (i * 2) + 2

    def parent(self, i):
        return int(math.ceil((i * 1.0) / 2)) - 1

    def swap(self, a, b):
        tmp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = tmp

    def heapify_down(self, i):
    	left = self.left(i)
    	right = self.right(i)
        # check if left child is smaller
    	if left <= self.last_index() and self.arr[left] < self.arr[i]:
    		smallest = left
    	else:
    		smallest = i
        # check if right child is smaller
    	if right <= self.last_index() and self.arr[right] < self.arr[smallest]:
    		smallest = right
        # call heapify if one of child is smaller
    	if smallest != i:
    		self.swap(i, smallest)
    		self.heapify_down(smallest)

    def heapify_up(self, i):
        parent = self.parent(i)
        if parent >= self.first_index() and self.arr[parent] > self.arr[i]:
            self.swap(parent, i)
            self.heapify_up(parent)

    def build_heap(self):
        for i in reversed(range(self.size / 2)):
            self.heapify_down(i)

    def peek(self):
        if self.size == 0:
            raise Exception('Heap is empty')
        return self.arr[self.first_index()]

    def pop(self):
        min_item = self.peek()
        self.swap(self.first_index(), self.last_index())
        del self.arr[self.last_index()]
        self.decrease_size()
        self.heapify_down(self.first_index())
        return min_item

    def push(self, item):
        self.arr.append(item)
        self.increase_size()
        self.heapify_up(self.last_index())

    def find_index(self, item):
        for i in range(self.size):
            if self.arr[i] == item:
                return i
        return None

    def find_and_heapify(self, item):
        index = self.find_index(item)
        self.heapify_up(index)
