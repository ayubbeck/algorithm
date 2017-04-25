class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print node.data
            self.inorder_walk(node.right)

    def preorder_walk(self, node):
        if node is not None:
            print node.data
            self.preorder_walk(node.left)
            self.preorder_walk(node.right)

    def find_parent(self, data):
        parent = None
        curr = self.root

        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return parent

    def find_parent_recursive(self, node, parent, data):
        if node is None:
            return parent
        if data < node.data:
            return self.find_parent_recursive(node.left, node, data)
        else:
            return self.find_parent_recursive(node.right, node, data)

    def insert(self, data):
        node = Node(data)
        parent = self.find_parent(data)
        # parent = self.find_parent_recursive(self.root, None, data)

        if parent is None:
            self.root = node
        elif data < parent.data:
            parent.left = node
        else:
            parent.right = node

        node.parent = parent

    def min(self, node):
        min = None

        while node is not None:
            min = node
            node = node.left

        return min

    def search(self, data):
        curr = self.root
        while curr is not None and data != curr.data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return curr

    def transplant(self, node, child):
        if node.parent is None:
            self.root = child
        elif node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child

        if child is not None:
            child.parent = node.parent

    def remove(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            min = self.min(node.right)
            if min.parent != node:
                self.transplant(min, min.right)
                min.right = node.right
                min.right.parent = min
            self.transplant(node, min)
            min.left = node.left
            min.left.parent = min
