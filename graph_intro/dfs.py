import sys

# Vertex
class Vertex:
    def __init__(self, id):
        self.id = id
        self.color = 'WHITE'
        self.distance = sys.maxint
        self.finish = sys.maxint
        self.prev = None

    def __str__(self):
        return str(self.id) + ' ' + str(self.color) + ' ' + str(self.distance) + '/' + str(self.finish)

# Depth First Search Graph
class Graph:
    def __init__(self, vertices, edges):
        self.time = 0
        self.vertices = self.init_vertices(vertices)
        self.edges = edges
        self.sorted_vertices = []

        for i in self.vertices:
            if self.vertices[i].color == 'WHITE':
                self.dfs_visit(self.vertices[i])

    def init_vertices(self, vertices):
        dict = {}
        for i in vertices:
            dict[i] = Vertex(i)
        return dict

    def dfs_visit(self, u):
        self.time = self.time + 1
        u.distance = self.time
        u.color = 'GRAY'
        for v in self.edges[u.id]:
            if self.vertices[v].color == 'WHITE':
                self.vertices[v].prev = u
                self.dfs_visit(self.vertices[v])
        u.color = 'BLACK'
        self.time = self.time + 1
        u.finish = self.time
        self.sorted_vertices.append(u)

    def topological_sort(self):
        s = ''
        for i in reversed(range(len(self.sorted_vertices))):
            s = s + str(self.sorted_vertices[i].id)
        return s
