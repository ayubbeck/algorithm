class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def add(self, data):
        node = Node(data)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, data):
        return self.search(data).data

    def search(self, data):
        curr = self.head.next
        while curr != self.head and curr.data != data:
            curr = curr.next

        return curr

    def remove_data(self, data):
        node = self.search(data)
        if node == self.head:
            raise Exception('Key does not exist')
        self.remove_node(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self):
        s = ''
        curr = self.head.next

        while curr != self.head:
            s = s + str(curr.data) + ' '
            curr = curr.next

        return s.strip()
