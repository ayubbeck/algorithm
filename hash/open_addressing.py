class Hash:
    def __init__(self, size = 5):
        self.size = size
        self.table = [None for i in range(0, size)]

    def linear_probing(self, key, i):
        hash_value = ((key % self.size) + i) % self.size
        return hash_value

    def quadratic_probing(self, key, i):
        hash_value = ((key % self.size) + (i * i)) % self.size
        return hash_value

    def get_hash_value(self, key, i):
        return self.linear_probing(key, i)
        # return self.quadratic_probing(key, i)

    def insert(self, key):
        i = 0
        while i < self.size:
            hash_value = self.get_hash_value(key, i)
            if self.table[hash_value] == None:
                self.table[hash_value] = key
                return hash_value
            else:
                i = i + 1

        raise Exception("Hash table is full")

    def remove(self, key):
        i = 0
        while i < self.size:
            hash_value = self.get_hash_value(key, i)
            if self.table[hash_value] == key:
                self.table[hash_value] = None
                return hash_value
            else:
                i = i + 1

        raise Exception("Key does not exist")

    def does_key_exist(self, key):
        i = 0
        while i < self.size:
            hash_value = self.get_hash_value(key, i)
            if self.table[hash_value] == key:
                return True
            else:
                i = i + 1

        return False
