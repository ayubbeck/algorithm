class Hash:
    def __init__(self, size = 11):
        self.size = size
        self.table = [None] * size

    def get_size(self):
        return self.size

    def get_hash_value(self, key):
        return key % self.size

    def get(self, key):
        return self.table[self.get_hash_value(key)]

    def set(self, key, data):
        hash_value = self.get_hash_value(key)
        self.table[hash_value] = data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.set(key, data)

    def __str__(self):
        items = ''
        for item in self.table:
            items = items + str(item) + ' '

        return items
