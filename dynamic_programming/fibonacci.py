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
