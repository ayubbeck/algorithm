import math

class RabinKarp:
    def __init__(self, text, pattern):
        self.prime = 11
        self.text = text
        self.pattern = pattern
        self.pattern_size = len(pattern)

    def get_initial_hash(self, text):
        hash_code = 0
        for i in range(0, len(text)):
            hash_code = hash_code + (ord(text[i]) * long(math.pow(self.prime, i)))
        return hash_code

    def get_hash(self, hash_code, prefix, suffix):
        return ((hash_code - ord(prefix)) / self.prime) + (ord(suffix) * long(math.pow(self.prime, self.pattern_size - 1)))

    def is_equal(self, text):
        if self.pattern == text:
            return True
        return False

    def process(self):
        init_hash = self.get_initial_hash(self.text[0:self.pattern_size])
        ptrn_hash = self.get_initial_hash(self.pattern)

        if init_hash == ptrn_hash:
            if self.is_equal(self.text[0:self.pattern_size]):
                return 0

        for i in range(0, len(self.text) - self.pattern_size):
            init_hash = self.get_hash(init_hash, self.text[i], self.text[i + self.pattern_size])
            if init_hash == ptrn_hash:
                if self.is_equal(self.text[i + 1:i + 1 + self.pattern_size]):
                    return i + 1

        return -1
