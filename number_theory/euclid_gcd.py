class Gcd:
    def __init__(self, a, b):
        self.gcd = self.gcd(a, b)
        self.gcd_extended = self.gcd_extended(a, b)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def gcd_extended(self, a, b):
        if b == 0:
            return a, 1, 0
        else:
            j, k, l = self.gcd_extended(b, a % b)
            d, x, y = (j, l, k - (a/b) * l)
            return d, x, y
