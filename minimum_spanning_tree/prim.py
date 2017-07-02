import sys

class Edge:
    def __init__(self, weight, node):
        self.w = weight
        self.n = node

    def __str__(self):
        return str(self.w)

class Vertex:
    def __init__(self, id, key):
        self.id = id
        self.key = key # weight to get to this node
        self.adj = [] # edges
        self.parent = None

    def __str__(self):
        return str(self.id) + ' ' + str(self.key)

class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = {}
        self.edges = []
        self.min_path = []
        self.total_weight = 0
        # Queue for unprocessed verticies.
        # Use Fibonacci Heap (PQ) here instead of array
        # for better performance on large items
        self.q = []
        # prim it
        self.prim(graph)

    def prim(self, vertices):
        # create vertices and put them in queue
        for vertex in vertices:
            node = Vertex(vertex, sys.maxint)
            self.vertices[vertex] = node
            self.q.append(node)
        # process vertices' edges and attachem them
        for vertex in vertices:
            for i in vertices[vertex]:
                key, value = i.popitem()
                edge = Edge(value, self.vertices[key])
                self.vertices[vertex].adj.append(edge)
        # start of the graph
        self.vertices[vertices.keys()[0]].key = 0
        # we are using array here instead of PQ
        # so we have to sort. Sorting takes O(nLogn)
        # that's why use PQ like Fibonacci Heap cuz it's mostly O(1) except for del item O(logn)
        self.q.sort(key=lambda vertex: vertex.key)
        # process the queue
        while self.q:
            u = self.q.pop(0)
            self.total_weight = self.total_weight + u.key
            # add vertecies to min path
            if u.parent is not None:
                self.min_path.append(u.parent.id + '->' + u.id)
            # process edges and make sure to update
            # the vertex key with the least amount of weight
            for edge in u.adj:
                if edge.n in self.q and edge.w < self.vertices[edge.n.id].key:
                    self.vertices[edge.n.id].parent = u
                    self.vertices[edge.n.id].key = edge.w
            # since we updated keys, sort again
            self.q.sort(key=lambda vertex: vertex.key)
