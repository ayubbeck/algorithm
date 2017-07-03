import sys
from Queue import Queue

# Vertex
class Vertex:
    def __init__(self, id):
        self.id = id
        self.color = 'WHITE'
        self.distance = sys.maxint
        self.prev = None

    def __str__(self):
        return str(self.id) + ' ' + str(self.color) + ' ' + str(self.distance)

# Breadth First Search Graph
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = self.init_vertices(vertices)
        self.edges = edges

        for i in self.vertices:
            if self.vertices[i].color == 'WHITE':
                self.bfs_visit(self.vertices['s'])

    def init_vertices(self, vertices):
        dict = {}
        for i in vertices:
            dict[i] = Vertex(i)

        return dict

    def bfs_visit(self, vertex):
        vertex.color = 'GRAY'
        vertex.distance = 0
        vertex.prev = None
        # this queue keeps trak of children
        q = Queue()
        q.put(vertex)
        # process each child
        while not q.empty():
            u = q.get()
            for v in self.edges[u.id]:
                if self.vertices[v].color == 'WHITE':
                    self.vertices[v].color = 'GRAY'
                    self.vertices[v].distance = u.distance + 1
                    self.vertices[v].prev = u
                    q.put(self.vertices[v])
            u.color = 'BLACK'

    def short_path(self, s, v, path=[]):
        if s == v:
            path.append(s.id)
        elif v.prev is None:
            path.append('no path from ' + s + ' to ' + v + ' exists')
        else:
            self.short_path(s, v.prev, path)
            path.append(v.id)
            return path
