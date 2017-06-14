import math
import copy

class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.left = None
        self.right = None
        self.parent = None
        self.child = None
        self.mark = False

    def __str__(self):
        return 'key: ' + str(self.key) + ' marked: ' + str(self.mark)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.right = self.head
        self.head.left = self.head

    def add(self, node):
        node.right = self.head.right
        node.right.left = node
        self.head.right = node
        node.left = self.head

    def remove(self, node):
        if node != self.head:
            node.left.right = node.right
            node.right.left = node.left

    def remove_all(self):
        self.head = Node(None)
        self.head.right = self.head
        self.head.left = self.head

    def search(self, key):
        node = self.head.right
        while node != self.head and node.key != key:
            node = node.right
        return node

    def display(self):
        node = self.head.right
        while node != self.head:
            print node
            node = node.right

    def link(self, y, x):
        self.remove(y)
        y.parent = x
        if x.child is None:
            x.child = y
            y.right = None
            y.left = None
        else:
            y.right = x.child
            y.left = None
            x.child.left = y
            x.child = y
        x.degree = x.degree + 1
        y.mark = False

class FibHeap:
    def __init__(self):
        self.root_list = DoublyLinkedList()
        self.min = None
        self.number = 0

    def peek(self):
        if self.min is None:
            return None
        else:
            return self.min.key

    def insert(self, key):
        node = Node(key)
        self.root_list.add(node)
        if self.min is None:
            self.min = node
        elif node.key < self.min.key:
            self.min = node
        self.number = self.number + 1

    def consolidate(self):
        height = int(math.ceil(math.log(self.number, 2)))
        arr = [None for _ in range(height)]
        w = self.root_list.head.right
        while w != self.root_list.head:
            x = copy.deepcopy(w)
            d = x.degree
            while arr[d] is not None:
                y = arr[d]
                if x.key > y.key:
                    temp = x
                    x = y
                    y = temp
                self.root_list.link(y, x)
                arr[d] = None
                d = d + 1
            arr[d] = x
            w = w.right
        self.min = None
        for i in range(height):
            if arr[i] is not None:
                if self.min is None:
                    self.root_list.remove_all()
                    self.root_list.add(arr[i])
                    self.min = arr[i]
                else:
                    self.root_list.add(arr[i])
                    if arr[i].key < self.min.key:
                        self.min = arr[i]

    def extract_min(self):
        node = self.min
        if node is not None:
            child = node.child
            while child is not None:
                next_child = child.right
                self.root_list.add(child)
                child.parent = None
                child = next_child
            self.root_list.remove(node)
            if node.right == self.root_list.head:
                if self.root_list.head.right == node:
                    self.min = None
                else:
                    self.min = self.root_list.head.right
            else:
                self.min = node.right
                self.consolidate()
            self.number = self.number - 1
        return node

    def cut(self, x, y):
        if x == y.child:
            y.child = x.right
            x.right.left = None
        else:
            x.left.right = x.right
            x.right.left = x.left
        x.parent = None
        x.mark = False
        self.root_list.add(x)

    def cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if node.mark == False:
                node.mark == True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise Exception('New key is greater than current key')
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)
        if node.key < self.min.key:
            self.min = node

    def delete(self, node):
        self.decrease_key(node, -9999999)
        self.extract_min()
