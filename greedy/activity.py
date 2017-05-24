class Activity:
    def __init__(self, items, start, finish):
        self.items = items
        self.start = start
        self.finish = finish

    def selector(self):
        k = 0
        items = [self.items[k] + 1]

        for m in range(1, len(self.start)):
            if self.start[m] >= self.finish[k]:
                items.append(self.items[m] + 1)
                k = m
        return items
