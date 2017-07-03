import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from graph_intro.dfs import Graph as DFS

class Vertex:
    def __init__(self, id):
        self.id = id
        self.d = sys.maxint
        self.p = None

    def __str__(self):
        return str(self.id) + ' ' + str(self.d) + ' ' + str(self.p)

class Graph:
    def __init__(self, vertices, edges, children, start):
        self.vertices = self.init_vertices(vertices, start)
        self.edges = edges
        # topologically order vertices
        self.sorted_vertices = DFS(vertices, children).sorted_vertices
        # run dag shprtest path
        self.dag()

    def init_vertices(self, vertices, start):
        dict = {}
        for i in vertices:
            dict[i] = Vertex(i)
        dict[start].d = 0
        return dict

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def dag(self):
        for u in reversed(self.sorted_vertices):
            for v, w in self.edges[u.id]:
                self.relax(self.vertices[u.id], self.vertices[v], w)

    def shortest_path(self, node):
        path = []
        while node is not None:
            path.append(node.id)
            node = node.p
        return list(reversed(path))
