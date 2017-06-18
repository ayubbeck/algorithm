import math

class VEB:
    def __init__(self, u):
        self.u = u
        self.clusters = [None for _ in range(int(math.sqrt(u)))]
        self.summary = None
        self.min = None
        self.max = None

    def high(self, x):
        return int(x / math.floor(math.sqrt(self.u)))

    def low(self, x):
        return int(x % math.floor(math.sqrt(self.u)))

    def index(self, x, y):
        return int(x * math.floor(math.sqrt(self.u))) + y

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            cluster = self.clusters[self.high(x)]
            if cluster is not None:
                return cluster.member(self.low(x))
            else:
                return False

    def empty_insert(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min is None:
            self.empty_insert(x)
        else:
            if x < self.min:
                temp = self.min
                self.min = x
                x = temp
            if self.u > 2:
                high = self.high(x)
                low = self.low(x)
                if self.clusters[high] is None:
                    self.clusters[high] = VEB(self.high(self.u))
                if self.summary is None:
                    self.summary = VEB(self.high(self.u))

                if self.clusters[high].min is None:
                    self.summary.insert(high)
                    self.clusters[high].empty_insert(low)
                else:
                    self.clusters[high].insert(low)
                if x > self.max:
                    self.max = x
                    
    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min is not None and x < self.min:
            return self.min
        else:
            high = self.high(x)
            low = self.low(x)
            maxlow = None
            if self.clusters[high] is not None:
                maxlow = self.clusters[high].max
            if maxlow is not None and low < maxlow:
                offset = self.clusters[high].successor(low)
                return self.index(high, offset)
            else:
                successor_cluster = None
                if self.summary is not None:
                    successor_cluster = self.summary.successor(high)
                if successor_cluster is None:
                    return None
                else:
                    offset = 0
                    if self.clusters[successor_cluster] is not None:
                        offset = self.clusters[successor_cluster].min
                    return self.index(successor_cluster, offset)
