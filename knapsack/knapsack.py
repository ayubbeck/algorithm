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

    def greedy_fill(self):
        curr_items = []
        curr_weight = 0
        curr_value = 0

        for i in range(self.items):
            curr_weight = curr_weight + self.weights[i]
            if curr_weight > self.capacity:
                overflow = curr_weight - self.capacity
                overflow_percentage = (overflow * 100) / self.weights[i]
                curr_value = curr_value + self.values[i] - (self.values[i] * overflow_percentage) / 100
                curr_items.append(str(100 - overflow_percentage) + '%')
                return curr_items, curr_weight, curr_value
            else:
                curr_items.append('100%')
                curr_value = curr_value + self.values[i]

        return curr_items, curr_weight, curr_value
