class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.right = self.head
        self.head.left = self.head

    def add(self, key):
        node = Node(key)
        node.right = self.head.right
        node.right.left = node
        self.head.right = node
        node.left = self.head

    def find(self, key):
        node = self.head.right
        while node != self.head and node.key != key:
            node = node.right
        return node

    def find_and_remove(self, key):
        node = self.head.right
        while node != self.head and node.key != key:
            node = node.right

        if node:
            self.remove(node)

    def remove(self, node):
        if node == self.head:
            raise Exception('Can not remove the head node')
        node.left.right = node.right
        node.right.left = node.left

    def peek(self, node, keys=[]):
        if node != self.head:
            self.peek(node.right, keys)
            keys.append(node.key)

        return keys
