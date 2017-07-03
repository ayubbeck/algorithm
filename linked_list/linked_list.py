# import sys
# from os import path
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
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
