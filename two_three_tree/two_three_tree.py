class Node:
    def __init__(self, keys, parent=None):
        self.keys = list([keys])
        self.child = list()
        self.parent = parent

    def __str__(self):
        return 'node keys: ' + str(self.keys)

    def __lt__(self, node):
        return self.keys[0] < node.keys[0]

    def _is_leaf(self):
        return len(self.child) == 0

    def _add(self, new_node):
        for child in new_node.child:
            child.parent = self

        self.keys.extend(new_node.keys)
        self.keys.sort()
        self.child.extend(new_node.child)

        if len(self.child) > 1:
            self.child.sort()
        if len(self.keys) > 2:
            self._split()

    def _insert(self, new_node):
        if self._is_leaf():
            self._add(new_node)
        elif new_node.keys[0] > self.keys[-1]:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.keys)):
                if new_node.keys[0] < self.keys[i]:
                    self.child[i]._insert(new_node)
                    break

    def _split(self):
        left_child = Node(self.keys[0], self)
        right_child = Node(self.keys[2], self)

        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.keys = [self.keys[1]]

        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._add(self)
        else:
            left_child.parent = self
            right_child.parent = self

    def _find(self, item):
        if item in self.keys:
            return item
        elif self._is_leaf():
            return False
        elif item > self.keys[-1]:
            return self.child[-1]._find(item)
        else:
            for i in range(len(self.keys)):
                if item < self.keys[i]:
                    return self.child[i]._find(item)

    def _preorder(self):
        print self
        for child in self.child:
            child._preorder()

class TwoThreeTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            self.root._insert(node)
            while self.root.parent:
                self.root = self.root.parent

        return True

    def find(self, item):
        return self.root._find(item)

    def preorder(self):
    	self.root._preorder()
