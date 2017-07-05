import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from heap_priority_queue.heap_priority_queue import HeapPriorityQueue as HeapPQ

class Vertex:
    def __init__(self, id):
        self.id = id
        self.d = sys.maxint
        self.p = None

    def __str__(self):
        return str(self.id) + ' ' + str(self.d)

    def __cmp__(self, other):
        if self.d < other.d:
            return -1
        elif self.d == other.d:
            return 0
        else:
            return 1

class Graph:
    def __init__(self, vertices, edges, start):
        self.vertices = self.init_vertices(vertices, start)
        self.edges = edges
        self.short_path = []
        self.dijkstra(start)

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
            return True
        return False

    def dijkstra(self, start):
        # create heap priority queue
        pq = HeapPQ()
        for i in self.vertices:
            pq.push(self.vertices[i])
        # process the priority queue
        while not pq.empty():
            u = pq.pop()
            self.short_path.append(u.id)
            for v, w in self.edges[u.id]:
                if self.relax(u, self.vertices[v], w):
                    pq.find_and_heapify(self.vertices[v])
