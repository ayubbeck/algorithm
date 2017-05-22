import sys

class Matrix:
    def __init__(self, arr):
        self.p = arr
        self.n = len(arr)
        self.m = [[0 for x in range(self.n)] for x in range(self.n)]
        self.s = [[0 for x in range(self.n)] for x in range(self.n)]
        self.path = ''

    def chain_order(self):
        for i in range(0, self.n):
            self.m[i][i] = 0

        for l in range(2, self.n):
            for i in range(1, self.n - l + 1):
                j = i + l - 1
                self.m[i][j] = sys.maxint
                for k in range(i, j):
                    q = self.m[i][k] + self.m[k + 1][j] + self.p[i - 1] * self.p[k] * self.p[j]
                    if q < self.m[i][j]:
                        self.m[i][j] = q
                        self.s[i][j] = k
        return self.m[1][self.n - 1], self.s[1][self.n - 1]

    def print_optimal_parens(self, s, i, j):
        if i == j:
            self.path = self.path + ('A' + str(i))
        else:
            self.path = self.path + ' ('
            self.print_optimal_parens(s, i, s[i][j])
            self.print_optimal_parens(s, s[i][j] + 1, j)
            self.path = self.path + ') '
