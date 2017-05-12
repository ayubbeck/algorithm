class Rod:
    def __init__(self, price):
        self.memo = {}
        self.price = price

    def cut(self, num):
        if num == 0:
            return 0
        max_revenue = -99999
        for i in range(1, num + 1):
            max_revenue = max(max_revenue, self.price[i] + self.cut(num - i))
        return max_revenue

    def memoized_cut(self, num):
        if num in self.memo:
            return self.memo[num]

        if num == 0:
            max_revenue = 0
        else:
            max_revenue = -99999
            for i in range(1, num + 1):
                max_revenue = max(max_revenue, self.price[i] + self.memoized_cut(num - i))
        if num not in self.memo:
            self.memo[num] = max_revenue

        return max_revenue

    def bottom_up_cut(self, num):
        self.memo[0] = 0
        for j in range(1, num + 1):
            max_revenue = -99999
            for i in range(1, j + 1):
                max_revenue = max(max_revenue, self.price[i] + self.memo[j - i])
            self.memo[j] = max_revenue
        return self.memo[num]
