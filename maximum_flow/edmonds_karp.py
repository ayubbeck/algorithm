import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from graph_intro.bfs import Graph as BFS

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity

    def __str__(self):
        return str(self.start) + '-' + str(self.end) + ': ' + str(self.capacity)

# Edmonds Karp (EK) algorithm for Ford Fulkerson (FF) Method
# FF does not define the path between the source to sink.
# It could be any path, longest or sortest. It does not matter.
# Where as EK uses only shortest path between the two by using Breadth First Search.
# Thus, EK O(VE^2) is faster than FF O(EF).
class Graph:
    def __init__(self, vertices, edges, source, sink):
        self.vertices = vertices
        self.source = source
        self.sink = sink
        self.flow = 0
        # create edges
        self.bfs_edges = {} # keep track BFS edges (residual edges)
        self.edges = {} # keep track original edges
        for i in vertices:
            for j, c in edges[i]:
                # add forward edge
                self.add_edge(i, j, c)
                # add backward edge
                self.add_edge(j, i, 0)
                self.add_bfs_edge(i, j)
        # calculate the max flow using Ford-Fulkerson method
        self.find_max_flow()

    def add_edge(self, start, end, capacity):
        index = self.get_index(start, end)
        self.edges[index] = Edge(start, end, capacity)

    def add_bfs_edge(self, start, end):
        if start not in self.bfs_edges:
            self.bfs_edges[start] = []
        self.bfs_edges[start].append(end)

    def remove_bfs_edge(self, start, end):
        for i, e in enumerate(self.bfs_edges[start]):
            if e == end:
                del self.bfs_edges[start][i]
                return

    def get_index(self, start, end):
        return start + '-' + end

    def get_flow(self, path):
        return min([self.edges[i].capacity for i in path])

    def create_residual_network(self, path, flow):
        for i in path:
            # reduce capacity
            self.edges[i].capacity = self.edges[i].capacity - flow
            # if edge's capacity is zero then remove it from residual network
            if self.edges[i].capacity == 0:
                self.remove_bfs_edge(self.edges[i].start, self.edges[i].end)
            self.add_bfs_edge(self.edges[i].end, self.edges[i].start)
            # get residual edge index
            index = self.get_index(self.edges[i].end, self.edges[i].start)
            # increase residual edge capacity
            self.edges[index].capacity = self.edges[index].capacity + flow

    def find_max_flow(self):
        # create BFS Graph and get a path
        bfs = BFS(self.vertices, self.bfs_edges, self.source)
        path = bfs.get_path(bfs.vertices[self.source], bfs.vertices[self.sink], [])
        while path:
            # print path
            # get/increment the flow that's going from start to sink
            flow = self.get_flow(path)
            self.flow = self.flow + flow
            # create residual edges
            self.create_residual_network(path, flow)
            bfs = BFS(self.vertices, self.bfs_edges, self.source)
            path = bfs.get_path(bfs.vertices[self.source], bfs.vertices[self.sink], [])
