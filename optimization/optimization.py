import sys

class Optimization:
    def __init__(self, arr, var):
        self.num_rows = len(arr)
        self.num_cols = len(arr[0])
        self.arr = arr
        self.num_of_var = var # number of variables
        self.profit = {}
        self.simplex()

    def simplex(self):
        # get pivot column
        col = self.get_pivot_col()
        # as long as there is room to improve keep simplexing
        while self.needs_more_optimization(col):
            # get pivor row
            row = self.get_pivot_row(col)
            # we want to make sure pivot is 1
            # otherwise turn it into 1 by dividing it by itself
            if self.arr[row][col] != 1:
                self.norm_pivot_row(row, col)
            # then, turn the rest of the rows of the pivot column into 0
            self.norm_other_row(row, col)
            # get column for next iteration
            col = self.get_pivot_col()
        # we are done with simplex method now.
        # so get the variable values and profit
        self.profit = self.get_result()

    def get_result(self):
        var = [0 for _ in range(self.num_of_var)]
        for i in range(self.num_rows - 1):
            for j in range(self.num_of_var):
                if self.arr[i][j] == 1:
                    if var[j] == 0:
                        var[j] = round(self.arr[i][self.num_cols - 1], 0)
                    else:
                        var[j] = 0
        return {'var': var, 'profit': self.arr[self.num_rows - 1][self.num_cols - 1]}

    def get_pivot_col(self):
        low = sys.maxint
        index = 0
        for i in range(self.num_of_var):
            if self.arr[self.num_rows - 1][i] < low:
                low = self.arr[self.num_rows - 1][i]
                index = i
        return index

    def get_pivot_row(self, col):
        low = sys.maxint
        index = 0
        for i in range(self.num_rows - 1):
            if self.arr[i][self.num_cols - 1] / self.arr[i][col] < low:
                low = self.arr[i][self.num_cols - 1] / self.arr[i][col]
                index = i
        return index

    def needs_more_optimization(self, col):
        return self.arr[self.num_rows - 1][col] < 0

    def norm_pivot_row(self, row, col):
        pivot = self.arr[row][col]
        for i in range(self.num_cols):
            self.arr[row][i] = self.arr[row][i] / pivot

    def norm_other_row(self, row, col):
        for i in range(self.num_rows):
            if i != row:
                pivot = self.arr[i][col] / self.arr[row][col]
                self.process_row(pivot, i, row)

    def process_row(self, pivot, row, pivot_row):
        for col in range(self.num_cols):
            self.arr[row][col] = self.arr[row][col] - (pivot * self.arr[pivot_row][col])
