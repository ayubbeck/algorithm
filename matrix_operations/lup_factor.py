class Matrix:
    # LUP factorization formulas
    # A * x = b
    # A = L * U
    # L * U * x = b
    # U * x = y
    # L * y = b
    def __init__(self, a, b):
        self.n = len(a)
        self.a = a
        self.b = b
        self.l = [[0 if i != j else 1 for i in a] for j in a]
        self.u = a
        self.y = [0 for _ in range(self.n)]
        self.x = [0 for _ in range(self.n)]
        # Find L and U. split A into Lower and Upper bound matrices
        # A = L * U
        self.lu_decompose()
        # find y. L * y = b
        self.find_y()
        # find x. U * x = y
        self.find_x()

    # takes O(n^3)
    def lu_decompose(self):
        for col in range(self.n):
            pivot = self.u[col][col]
            for row in range(col + 1, self.n):
                low = self.u[row][col] / pivot
                self.l[row][col] = low
                for v in range(col, self.n):
                    self.u[row][v] = self.u[row][v] - low * self.u[col][v]
    # takes O(n^2)
    def find_y(self):
        for row in range(self.n):
            sum = 0
            for col in range(self.n):
                if row != col:
                    sum = sum + (self.l[row][col] * self.y[col])
                else:
                    self.y[row] = self.b[row] - sum
                    break
    # takes O(n^2)
    def find_x(self):
        for row in reversed(range(self.n)):
            sum = 0
            for col in reversed(range(self.n)):
                if row != col:
                    sum = sum + (self.u[row][col] * self.x[col])
                else:
                    self.x[row] = (self.y[row] - sum) / self.u[row][col]
                    break
