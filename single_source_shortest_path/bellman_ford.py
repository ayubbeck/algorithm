import sys

class Vertex:
    def __init__(self, id):
        self.id = id
        self.d = sys.maxint
        self.p = None

class Graph:
    def __init__(self, vertices, edges, start):
        self.vertices = self.init_single_source(vertices, start)
        self.edges = edges

    def init_single_source(self, vertices, start):
        dict = {}
        # init verteces
        for i in vertices:
            dict[i] = Vertex(i)
        # start vertex will have 0 for distance
        dict[start].d = 0
        return dict

    def relax(self, u, v, w):
        # update destination vertex distance (v) if v distance is larger than
        # parent distance + edge weight
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def bellman_ford(self):
        # process the edges
        for i in range(len(self.vertices) - 1):
            for u, v, w in self.edges:
                self.relax(self.vertices[u], self.vertices[v], w)
        # check for negative weigth cycle
        for u, v, w in self.edges:
            if self.vertices[v].d > self.vertices[u].d + w:
                return False
        return True

    def shortest_path(self, node):
        path = []
        # follow the vertices' parents
        #  to get the path
        while node is not None:
            path.append(node.id)
            node = node.p
        return list(reversed(path))
