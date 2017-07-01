class Edge:
    def __init__(self, weight, node_a, node_b):
        self.weight = weight
        self.a = node_a
        self.b = node_b

    def __str__(self):
        return str(self.weight) + ': ' + str(self.a) + '-' + str(self.b)

class Vertex:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.rank = None

    def __str__(self):
        return str(self.key)

class Kruskal:
    def __init__(self, vertices):
        self.vertices = {}
        self.edges = []
        self.min_path = []
        self.kruskal(vertices)

    def kruskal(self, vertices):
        # create vertecies and make set out of them
        for vertex in vertices:
            node = Vertex(vertex)
            self.vertices[vertex] = node
            self.make_set(node)
        # create edges
        for vertex in vertices:
            for i in vertices[vertex]:
                v, w = i.popitem()
                edge = Edge(w, self.vertices[vertex], self.vertices[v])
                self.edges.append(edge)
        # sort edges in increasing order
        self.edges.sort(key=lambda edge: edge.weight)
        # find min path
        for edge in self.edges:
            if not self.same_component(edge.a, edge.b):
                self.min_path.append(edge)
                self.union(edge.a, edge.b)

    def make_set(self, node):
        node.p = node
        node.rank = 0

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
