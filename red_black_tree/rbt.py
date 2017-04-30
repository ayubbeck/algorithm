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

    def min(self, node):
        min = node
        while node != self.dummy:
            min = node
            node = node.left
        return min

    def search(self, data):
        curr = self.root
        node = self.dummy

        while curr != self.dummy and data != curr.data:

            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

            node = curr

        return node

    def transplant(self, node, child):
        if node.parent == self.dummy:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.parent = node.parent

    def delete(self, node):
        temp = node
        temp_orig_color = temp.color

        if node.left == self.dummy:
            start_fixup = node.right
            self.transplant(node, node.right)
        elif node.right == self.dummy:
            start_fixup = node.left
            self.transplant(node, node.left)
        else:
            temp = self.min(node.right)
            temp_orig_color = temp.color
            start_fixup = temp.right

            if temp.parent == node:
                start_fixup.parent = temp
            else:
                self.transplant(temp, temp.right)
                temp.right = node.right
                temp.right.parent = temp
            self.transplant(node, temp)
            temp.left = node.left
            temp.left.parent = temp
            temp.color = node.color

        if temp_orig_color == 'BLACK':
            self.delete_fixup(start_fixup)

    def delete_fixup(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                node_sibling = node.parent.right
                if node_sibling.color == 'RED':
                    node_sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.left_rotate(node.parent)
                    node_sibling = node.parent.right
                if node_sibling.left.color == 'BLACK' and node_sibling.right.color == 'BLACK':
                    node_sibling.color = 'RED'
                    node = node.parent
                else:
                    if node_sibling.right.color == 'BLACK':
                        node_sibling.left.color = 'BLACK'
                        node_sibling.color = 'RED'
                        self.right_rotate(node_sibling)
                        node_sibling = node.parent.right
                    node_sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    node_sibling.right.color = 'BLACK'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                node_sibling = node.parent.left
                if node_sibling.color == 'RED':
                    node_sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.right_rotate(node.parent)
                    node_sibling = node.parent.left
                if node_sibling.left.color == 'BLACK' and node_sibling.right.color == 'BLACK':
                    node_sibling.color = 'RED'
                    node = node.parent
                else:
                    if node_sibling.left.color == 'BLACK':
                        node_sibling.right.color = 'BLACK'
                        node_sibling.color = 'RED'
                        self.left_rotate(node_sibling)
                        node_sibling = node.parent.left
                    node_sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    node_sibling.left.color = 'BLACK'
                    self.right_rotate(node.parent)
                    node = self.root
