import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from single_source_shortest_path.bellman_ford import Graph as BellmanFord
from single_source_shortest_path.dijkstra import Graph as Dijkstra

class Graph:
    def __init__(self, vertices, edges):
        self.start = 's'
        self.vertices = vertices
        self.edges = edges
        self.dijkstra_edges = {}
        self.dist = [[0 for i in range(len(vertices))] for j in range(len(vertices))]
        self.next = [[None for i in range(len(vertices))] for j in range(len(vertices))]
        # run bellman ford
        # vertices + self.start and edges + (s for each vertex)
        self.bf = BellmanFord(self.augment_vertices(), self.augment_edges(), self.start)
        if not self.bf.bellman_ford():
            print 'has negative weight cycle'
        else:
            # pop the extra vertex
            self.bf.vertices.pop(self.start)
            # reweight the edges
            for u, v, w in self.edges:
                # re-calculate weighted edge
                reweighted_edge = w + self.bf.vertices[u].d - self.bf.vertices[v].d
                # store re-calculate weighted edge
                if u in self.dijkstra_edges:
                    self.dijkstra_edges[u].append([v, reweighted_edge])
                else:
                    self.dijkstra_edges[u] = []
                    self.dijkstra_edges[u].append([v, reweighted_edge])
            # run thru Dijkstra's and put them in the dist and next matrices
            dj_vertices = [v for v in self.vertices]
            for u in self.vertices:
                # run Dijkstra
                dj = Dijkstra(dj_vertices, self.dijkstra_edges, u)
                # populate matrices
                for v in self.vertices:
                    self.dist[self.vertices[u]][self.vertices[v]] = dj.vertices[v].d + \
                    self.bf.vertices[v].d - self.bf.vertices[u].d
                    self.next[self.vertices[u]][self.vertices[v]] = dj.vertices[v].p.id if dj.vertices[v].p else None

    def augment_vertices(self):
        l = [v for v in self.vertices]
        # add extra vertex
        return list(set(l).union([self.start]))

    def augment_edges(self):
        # add edges for extra vertex and to the rest of vertices
        l = []
        for e in self.edges:
            l.append(e)
        for v in self.vertices:
            l.append([self.start, v, 0])
        return l

    def shortest_path(self, u, v):
        shortest_path = [v]
        # get the next vertex
        next_v = self.next[self.vertices[u]][self.vertices[v]]
        shortest_path.append(next_v)
        # check if shortest path is between the same vertices
        if next_v is None:
            return [u]
        # move onto the next one
        while next_v != u:
            next_v = self.next[self.vertices[u]][self.vertices[next_v]]
            shortest_path.append(next_v)
        # return reversed path
        return list(reversed(shortest_path))

    def shortest_dist(self, u, v):
        return self.dist[self.vertices[u]][self.vertices[v]]
