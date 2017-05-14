import sys

class Matrix:
    def __init__(self, arr):
        self.p = arr
        self.n = len(arr)

    def chain_order(self):
        m = [[0 for x in range(self.n)] for x in range(self.n)]
        s = [[0 for x in range(self.n)] for x in range(self.n)]

        for i in range(1, self.n):
            m[i][i] = 0

        for l in range(2, self.n):
            for i in range(1, self.n - l + 1):
                j = i + l - 1
                m[i][j] = sys.maxint
                for k in range(i, j):
                    q = m[i][k] + m[k + 1][j] + self.p[i - 1] * self.p[k] * self.p[j]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k

        return m[1][self.n - 1], s[1][self.n - 1]
