import sys

class Graph:
    def __init__(self, vertices, edges):
        self.size = len(vertices) if vertices else 0
        self.vertices = vertices
        self.edges = edges
        self.dist = [[sys.maxint for _ in range(self.size)] for _ in range(self.size)]
        self.next = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.floyd_warshall()

    def floyd_warshall(self):
        # path between two same vertices is 0
        for v in self.vertices:
            self.dist[self.vertices[v]][self.vertices[v]] = 0
        # populate distance and next matrices with default values
        for v in self.edges:
            for e, w in self.edges[v]:
                self.dist[self.vertices[v]][self.vertices[e]] = w
                self.next[self.vertices[v]][self.vertices[e]] = v
        # this runs on O(v^3)
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    d = sys.maxint
                    # relax the weight
                    if self.dist[i][k] != sys.maxint:
                        d = self.dist[i][k] + self.dist[k][j]
                    if self.dist[i][j] > d:
                        self.dist[i][j] = d
                        self.next[i][j] = self.next[k][j]

    def shortest_path(self, u, v):
        shortest_path = [v]
        # get the next vertex
        next_v = self.next[self.vertices[u]][self.vertices[v]]
        shortest_path.append(next_v)
        # move onto the next one
        while next_v != u:
            next_v = self.next[self.vertices[u]][self.vertices[next_v]]
            shortest_path.append(next_v)
        # return reversed path
        return list(reversed(shortest_path))
