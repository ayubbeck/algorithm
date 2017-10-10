class SMFA:
    def __init__(self, text, pattern, chars):
        self.text = text
        self.pattern = pattern
        self.chars = chars
        self.delta = [[0 for _ in range(len(self.chars))] for _ in range(len(self.pattern) + 1)]
        self.char_hash = self.hash_chars()
        self.shifts = []
        self.preprocess()
        self.match()

    def preprocess(self):
        m = len(self.pattern)
        for q in range(m + 1):
            for a in self.chars:
                k = min(m + 1, q + 2) - 1
                while not self.is_suffix(k, q, a):
                    k = k - 1
                self.delta[q][self.char_hash[a]] = k

    def is_suffix(self, k, q, a):
        suffix = self.pattern[0:k]
        text = self.pattern[0:q] + a
        # empty string is suffix of any string
        if suffix == '':
            return True
        # check the suffix
        k = len(suffix) * -1
        if text[k:] == suffix:
            return True
        else:
            return False

    def match(self):
        n = len(self.text)
        m = len(self.pattern)
        q = 0
        for i in range(n):
            q = self.delta[q][self.char_hash[self.text[i]]]
            if q == m:
                self.shifts.append((i - m) + 1)

    def print_delta(self):
        for i in self.delta:
            print i

    def hash_chars(self):
        char_hash = {}
        count = 0
        for i in self.chars:
            char_hash[i] = count
            count = count + 1
        return char_hash
