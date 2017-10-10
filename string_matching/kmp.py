class KnuthMorrisPratt:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.shifts = []
        self.match()

    def compute_prefix(self):
        m = len(self.pattern) + 1
        py = [0 for _ in range(m)]
        k = 0
        for q in range(2, m):
            while k > 0 and self.pattern[k] != self.pattern[q - 1]:
                k = py[k]
            if self.pattern[k] == self.pattern[q - 1]:
                k = k + 1
            py[q] = k
        return py

    def match(self):
        n = len(self.text)
        m = len(self.pattern)
        py = self.compute_prefix()
        q = 0 # number of chars matched
        for i in range(n):
            while q > 0 and self.pattern[q] != self.text[i]:
                q = py[q] # next char does not matched
            if self.pattern[q] == self.text[i]:
                q = q + 1
            if q == m:
                self.shifts.append(i - m + 1)
                q = py[q]
