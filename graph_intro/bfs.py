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

    def __str__(self):
        return str(self.key) + ' ' + str(self.color) + ' ' + str(self.distance)

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, key):
        node = Vertex(key)
        node.next = self.head
        self.head = node

class BFS:
    def __init__(self):
        self.adj = []

    def bfs(self, start):
        # starter process
        self.adj[start].head.color = 'GRAY'
        self.adj[start].head.distance = 0
        self.adj[start].head.prev = None
        # this queue keeps trak of children
        q = Queue()
        q.put(self.adj[start].head)
        # process each child
        while not q.empty():
            v = q.get()
            # parent's distance, child's distance will be parent's distance + 1
            size = v.distance
            u = v.next
            while u is not None:
                i = u.key - 1
                if self.adj[i].head.color == 'WHITE':
                    self.adj[i].head.color = 'GRAY'
                    self.adj[i].head.distance = size + 1
                    self.adj[i].head.prev = v
                    q.put(self.adj[i].head)
                u = u.next
            v.color = 'BLACK'

    def short_path(self, s, v, path=[]):
        if s == v:
            path.append(s.key)
        elif v.prev is None:
            path.append('no path from ' + s + ' to ' + v + ' exists')
        else:
            self.short_path(s, v.prev, path)
            path.append(v.key)
            return path
