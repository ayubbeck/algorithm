class Knapsack:
    def __init__(self, capacity, weights, values):
        self.items = len(weights)
        self.weights = weights #weights of the items
        self.values = values # values of the items
        self.capacity = capacity # capacity of the knapsack
        # the keep variable keeps track of what we are taking and what we are not taking
        self.keep = [[0 for i in range(self.capacity)] for j in range(self.items)]

    '''
        This Dynamic Programming implementation of 0/1 Knapsack problem.
        It processes each item in bottom-up fashion and finds optimal
        solution for each subproblems first. And as it goes towards the top
        it finds the optimal solution globally using already found optimal
        solutions for the subproblems.
    '''
    def fill(self):
        # value table
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

    '''
        Once we have the val and keep tables ready,
        we simply extract the items we want to take
    '''
    def get_items(self):
        cap = self.capacity - 1
        items = []
        for i in reversed(range(1, self.items)):
            if self.keep[i][cap] == 1:
                cap = cap - 1
                items.append(i)

        return items

    '''
        This is greedy algorithm implementation of the problem.
        it loops thru the sorted item (sorted by value) and takes the
        whole item unless there is no enough space in the knapsack.
        if there is only space for the fraction of the item then we
        will take that fraction.
    '''
    def greedy_fill(self):
        curr_items = []
        curr_weight = 0
        curr_value = 0

        for i in range(self.items):
            # keeping track of the weight of the items  we already took
            curr_weight = curr_weight + self.weights[i]
            if curr_weight > self.capacity:
                # so here we dont have space for the whole item, so
                # we will do some math to get what the fraction we are taking
                overflow = curr_weight - self.capacity
                overflow_percentage = (overflow * 100) / self.weights[i]
                curr_value = curr_value + self.values[i] - (self.values[i] * overflow_percentage) / 100
                curr_items.append(str(100 - overflow_percentage) + '%')
                return curr_items, curr_weight, curr_value
            else:
                # we taking the whole item
                curr_items.append('100%')
                curr_value = curr_value + self.values[i]

        return curr_items, curr_weight, curr_value
