class Fibonacci:
    def __init__(self):
        self.memo = {}

    def calc(self, n):
        if n <= 2:
            output = 1
        else:
            output = self.calc(n - 1) + self.calc(n - 2)

        return output

    def memoized_calc(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 2:
            output = 1
        else:
            output = self.memoized_calc(n - 1) + self.memoized_calc(n - 2)

        if n not in self.memo:
            self.memo[n] = output

        return output

    def buttom_up_calc(self, n):
        self.memo[0] = 0
        self.memo[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                self.memo[0] = self.memo[0] + self.memo[1]
            else:
                self.memo[1] = self.memo[0] + self.memo[1]

        if self.memo[0] > self.memo[1]:
            return self.memo[0]
        else:
            return self.memo[1]
