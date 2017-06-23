class Node:
    def __init__(self, key):
        self.p = None
        self.rank = None
        self.key = key

    def __str__(self):
        return str(self.key)

class DisjointSet:
    def __init__(self, keys):
        self.keys = keys
        self.sets = []

    def connected_components(self):
        for key in self.keys:
            node = Node(key)
            self.sets.append(node)
            self.make_set(node)

        size = len(self.sets)
        for i in range(size):
            if i + 1 < size:
                if not self.same_component(self.sets[i], self.sets[i + 1]):
                    self.union(self.sets[i], self.sets[i + 1])

    def make_set(self, x):
        x.p = x
        x.rank = 0

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank = y.rank + 1

    def find_set(self, x):
        if x != x.p:
            x.p = self.find_set(x.p)
        return x.p

    def same_component(self, x, y):
        if self.find_set(x) == self.find_set(y):
            return True
        return False
