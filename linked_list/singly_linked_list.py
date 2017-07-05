class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node

    def find(self, key):
        node = self.head
        while node is not None and node.key != key:
            node = node.next
        return node

    def find_prev(self, key):
        prev = None
        node = self.head
        while node is not None and node.key != key:
            prev = node
            node = node.next
        return node, prev

    def remove(self, key):
        node, prev = self.find_prev(key)
        if node:
            if prev:
                prev.next = node.next
            else:
                self.head = node.next

    def peek(self, node, keys=[]):
        if node is not None:
            self.peek(node.next, keys)
            keys.append(node.key)

        return keys
