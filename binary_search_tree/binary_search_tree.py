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

    def insert(self, data):
        parent_node = None
        new_node = Node(data)
        curr_node = self.root

        while curr_node is not None:
            parent_node = curr_node
            if new_node.data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        new_node.parent = parent_node

        if parent_node is None:
            self.root = new_node
        elif new_node.data < parent_node.data:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print node
            self.inorder_tree_walk(node.right)

    def search(self, node, data):
        if node is None or data == node.data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def min(self, node):
        min = None
        while node is not None:
            min = node
            node = node.left

        return min

    def transplant(self, node, child):
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
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
