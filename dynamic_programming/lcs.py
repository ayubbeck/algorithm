class Lcs:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.b = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]
        self.c = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]

    def print_it(self):
        for i in range(len(self.x) + 1):
            for j in range(len(self.y) + 1):
                print self.c[i][j],
            print

    def print_lines(self):
        for i in range(len(self.x) + 1):
            for j in range(len(self.y) + 1):
                print self.b[i][j],
            print

    def length(self):
        for i in range(1, len(self.x) + 1):
            for j in range(1, len(self.y) + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.c[i][j] = self.c[i - 1][j - 1] + 1
                    self.b[i][j] = '\\'
                else:
                    if self.c[i - 1][j] >= self.c[i][j - 1]:
                        self.c[i][j] = self.c[i - 1][j]
                        self.b[i][j] = '|'
                    else:
                        self.c[i][j] = self.c[i][j - 1]
                        self.b[i][j] = '-'
        return self.c, self.b

    def print_lcs(self, b, x, i, j):
        if i == 0 or j == 0:
            return
        if b[i][j] == '\\':
            self.print_lcs(b, x, i - 1, j - 1)
            print x[i - 1],
        elif b[i][j] == '|':
            self.print_lcs(b, x, i - 1, j)
        else:
            self.print_lcs(b, x, i, j - 1)
