class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        return '{} {}'.format(str(self.data), self.color)

class RedBlackTree:
    def __init__(self):
        self.dummy = Node(None)
        self.dummy.color = 'BLACK'
        self.root = self.dummy

    def left_rotate(self, node):
        temp = node.right
        node.right = temp.left

        if temp.left != self.dummy:
            temp.left.parent = node

        temp.parent = node.parent

        if node.parent == self.dummy:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.left = node
        node.parent = temp

    def right_rotate(self, node):
        temp = node.left
        node.left = temp.right

        if temp.right != self.dummy:
            temp.right.parent = node

        temp.parent = node.parent

        if node.parent == self.dummy:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.right = node
        node.parent = temp

    def add(self, data):
        node = Node(data)
        parent = self.dummy
        curr = self.root

        while curr != self.dummy:
            parent = curr
            if node.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = parent
        if parent == self.dummy:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        node.left = self.dummy
        node.right = self.dummy
        node.color = 'RED'

        self.fix_tree(node)

    def fix_tree(self, node):
        while node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                temp = node.parent.parent.right
                if temp.color == 'RED':
                    node.parent.color = 'BLACK'
                    temp.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                temp = node.parent.parent.left
                if temp.color == 'RED':
                    node.parent.color = 'BLACK'
                    temp.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            print node if node.data is not None else ''
            self.inorder_walk(node.right)
