class Knapsack:
    def __init__(self, capacity, weights, values):
        self.items = len(weights)
        self.weights = weights
        self.values = values
        self.capacity = capacity

        self.keep = [[0 for i in range(self.capacity)] for j in range(self.items)]

    def fill(self):
        val = [[0 for i in range(self.capacity)] for j in range(self.items)]

        for i in range(1, self.items):
            for j in range(self.capacity):
                curr_cap = j + 1
                if self.weights[i] > curr_cap:
                    val[i][j] = val[i - 1][j]
                else:
                    remainder = 0 if j - self.weights[i] < 0 else j - self.weights[i]
                    if self.values[i] + val[i - 1][remainder] > val[i - 1][j]:
                        val[i][j] = self.values[i] + val[i - 1][remainder]
                        self.keep[i][j] = 1
                    else:
                        val[i][j] = val[i - 1][j]

    def get_items(self):
        cap = self.capacity - 1
        items = []
        for i in reversed(range(1, self.items)):
            if self.keep[i][cap] == 1:
                cap = cap - 1
                items.append(i)

        return items
