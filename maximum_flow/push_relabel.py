import sys

class Vertex:
    def __init__(self, id, height=0, excess=0):
        self.id = id
        self.height = height
        self.excess = excess

    def __str__(self):
        return str(self.id) + ': ' + str(self.height) + '/' + str(self.excess)

    def increase_excess(self, flow):
        self.excess = self.excess + flow

    def decrease_excess(self, flow):
        self.excess = self.excess - flow

    def increase_height(self, height):
        self.height = self.height + 1

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity

    def __str__(self):
        return str(self.start) + '-' + str(self.end) + ': ' + str(self.capacity)

    def increase_capacity(self, capacity):
        self.capacity = self.capacity + capacity

    def decrease_capacity(self, capacity):
        self.capacity = self.capacity - capacity

class Graph:
    def __init__(self, vertices, edges, source, sink):
        self.source = source
        self.sink = sink
        self.vertices = {}
        self.edges = {}
        self.residual_network = {}
        # init vertices and edges
        for start in vertices:
            # create Vertex
            self.vertices[start] = Vertex(start)
            for end, capacity in edges[start]:
                # create both forward and backward edges for these vertices
                self.add_edge(start, end, capacity)
                self.add_edge(end, start, 0)
                # add the edge to residual network
                self.insert_residual_edge(start, end)
        # run unit preflow
        self.init_preflow(edges[source])
        # find max flow
        self.find_max_flow()

    def get_index(self, start, end):
        return start + '-' + end

    def add_edge(self, start, end, capacity):
        index = self.get_index(start, end)
        self.edges[index] = Edge(start, end, capacity)

    def insert_residual_edge(self, start, end):
        if start not in self.residual_network:
            self.residual_network[start] = []
        if end not in self.residual_network[start]:
            self.residual_network[start].append(end)

    def remove_residual_edge(self, start, end):
        for i, e in enumerate(self.residual_network[start]):
            if e == end:
                del self.residual_network[start][i]
                return

    def update_residual_network(self, start, end):
        index = self.get_index(start, end)
        if self.edges[index].capacity == 0:
            self.remove_residual_edge(start, end)
        else:
            self.insert_residual_edge(start, end)

    def push(self, start, end):
        # get indexes
        edge_index = self.get_index(start, end)
        residual_index = self.get_index(end, start)
        # get flow
        flow = min(self.vertices[start].excess, self.edges[edge_index].capacity)
        # update vertex excess
        self.vertices[start].excess = self.vertices[start].excess - flow
        self.vertices[end].excess = self.vertices[end].excess + flow
        # update edges
        self.edges[edge_index].decrease_capacity(flow)
        self.edges[residual_index].increase_capacity(flow)
        # update residual network
        self.update_residual_network(start, end)
        self.update_residual_network(end, start)

    def relabel(self, start, height):
        self.vertices[start].increase_height(height)

    def init_preflow(self, neighbors):
        # set up source height
        self.vertices[self.source].height = len(self.vertices)
        # push the flow for each neighbor
        for neighbor, flow in neighbors:
            # update vertex excess
            self.vertices[neighbor].excess = flow
            self.vertices[self.source].decrease_excess(flow)
            # update residual network
            self.insert_residual_edge(neighbor, self.source)
            self.remove_residual_edge(self.source, neighbor)
            # update edge capacity after the flow
            self.edges[self.get_index(neighbor, self.source)].capacity = flow
            self.edges[self.get_index(self.source, neighbor)].capacity = 0

    def get_vertex_with_positive_excess(self):
        excess = 0
        for v in self.vertices:
            if v != self.sink and self.vertices[v].excess > excess:
                return v
        return None

    def get_low_neighbor(self, start):
        height = sys.maxint
        low = None
        for i in self.residual_network[start]:
            if self.vertices[i].height < height:
                low = i
                height = self.vertices[i].height
        return low

    def find_max_flow(self):
        start = self.get_vertex_with_positive_excess()
        while start is not None:
            end = self.get_low_neighbor(start)
            self.relabel(start, self.vertices[end].height)
            self.push(start, end)
            start = self.get_vertex_with_positive_excess()
