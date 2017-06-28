# Breadth First Search
import sys
from Queue import Queue

class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = 'WHITE'
        self.distance = sys.maxint
        self.prev = None
        self.next = None
        self.adj = None

    def __str__(self):
        s = ''
        node = self.adj.head
        while node is not None:
            s = s + str(node.key)
            node = node.next
        return 'distance: ' + str(self.distance) + ', key: ' + str(self.key) + \
               ', children: ' + s + ', color: ' + str(self.color)

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, key):
        node = Vertex(key)
        node.next = self.head
        self.head = node

class BFS:
    def __init__(self, graph):
        self.vertices = {}
        self.graph_it(graph)

        for i in self.vertices:
            if self.vertices[i].color == 'WHITE':
                self.bfs_visit(self.vertices['s'])

    def graph_it(self, graph):
        for item in graph:
            self.vertices[item] = Vertex(item)

        for i in graph:
            l = LinkedList()
            for j in graph[i]:
                l.add(j)
            self.vertices[i].adj = l

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
            # child's distance will be parent's distance + 1
            size = u.distance
            v = u.adj.head
            while v is not None:
                if self.vertices[v.key].color == 'WHITE':
                    self.vertices[v.key].color = 'GRAY'
                    self.vertices[v.key].distance = size + 1
                    self.vertices[v.key].prev = u
                    q.put(self.vertices[v.key])
                v = v.next
            u.color = 'BLACK'

    def short_path(self, s, v, path=[]):
        if s == v:
            path.append(s.key)
        elif v.prev is None:
            path.append('no path from ' + s + ' to ' + v + ' exists')
        else:
            self.short_path(s, v.prev, path)
            path.append(v.key)
            return path
