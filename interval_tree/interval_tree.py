
class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

class Node:
    def __init__(self, low, high):
        self.interval = Interval(low, high)
        self.left = None
        self.right = None
        self.max = None
        self.color = None

    def __str__(self):
        return '[{}-{}] {} {}'.format(
            str(self.interval.low),
            str(self.interval.high),
            str(self.max),self.color
        )

class IntervalTree:
    def __init__(self):
        self.dummy = Node(None, None)
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

        temp.max = max(temp.max, temp.left.max, temp.right.max)

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

        temp.max = max(temp.max, temp.left.max, temp.right.max)

    def add(self, low, high):
        node = Node(low, high)
        node.max = high
        parent = self.dummy
        curr = self.root

        while curr != self.dummy:
            parent = curr
            if parent.max is None:
                parent.max = node.interval.high
            elif parent.max < node.interval.high:
                parent.max = node.interval.high

            if node.interval.low < curr.interval.low:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = parent
        if parent == self.dummy:
            self.root = node
        elif node.interval.low < parent.interval.low:
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
            print node if node.max is not None else ''
            self.inorder_walk(node.right)

    def __check_overlap(self, a, b):
        overlaps = False
        if a.low < b.low and a.high >= b.low and a.high <= b.high:
            overlaps = True
        elif a.high > b.high and a.low >= b.low and a.low <= b.high:
            overlaps = True
        return overlaps

    def search(self, interval):
        curr = self.root
        while curr != self.dummy and not self.__check_overlap(interval, curr.interval):
            if curr.left != self.dummy and curr.left.max >= interval.low:
                curr = curr.left
            else:
                curr = curr.right
        return curr
