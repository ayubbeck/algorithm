from doubly_linked_list import DoublyLinkedList

class Hash:
    def __init__(self, size = 11):
        self.size = size
        self.table = [DoublyLinkedList() for i in range(size)]

    def get_size(self):
        return self.size

    def get_hash_value(self, key):
        if type(key) not in (str, int):
            raise Exception("keys can be either str or int")
        # calc hash value for str
        if type(key) is str:
            sum = 0
            for i in list(key):
                sum = sum + ord(i)
            return sum % self.size
        # calc hash value for int
        return key % self.size

    def add(self, key):
        hash_value = self.get_hash_value(key)
        self.table[hash_value].add(key)

    def get(self, key):
        hash_value = self.get_hash_value(key)
        return self.table[hash_value].get(key)

    def remove(self, key):
        hash_value = self.get_hash_value(key)
        self.table[hash_value].remove_data(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.add(key, data)

    def __str__(self):
        items = ''
        for item in self.table:
            print item
            # items = items + str(item) + ' '

        return ''
