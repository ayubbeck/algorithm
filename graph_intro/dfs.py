# Depth First Search
import sys
from Queue import Queue

class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = 'WHITE'
        self.distance = sys.maxint
        self.finish = sys.maxint
        self.prev = None
        self.next = None
        self.adj = None

    def __str__(self):
        return str(self.key) + ' ' + str(self.color) + ' ' + str(self.distance) + '/' + str(self.finish)

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, key):
        node = Vertex(key)
        node.next = self.head
        self.head = node

class DFS:
    def __init__(self, graph):
        self.vertices = {}
        self.time = 0
        self.sorted_vertices = []

        for item in graph:
            self.vertices[item] = Vertex(item)

        for i in graph:
            l = LinkedList()
            for j in graph[i]:
                l.add(j)
            self.vertices[i].adj = l

        for i in self.vertices:
            if self.vertices[i].color == 'WHITE':
                self.dfs_visit(self.vertices[i])

    def dfs_visit(self, u):
        self.time = self.time + 1
        u.distance = self.time
        u.color = 'GRAY'
        v = u.adj.head
        while v is not None:
            if self.vertices[v.key].color == 'WHITE':
                self.vertices[v.key].prev = u
                self.dfs_visit(self.vertices[v.key])
            v = v.next
        u.color = 'BLACK'
        self.time = self.time + 1
        u.finish = self.time
        self.sorted_vertices.append(u)

    def topological_sort(self):
        s = ''
        for i in reversed(range(len(self.sorted_vertices))):
            s = s + str(self.sorted_vertices[i].key)
        return s
