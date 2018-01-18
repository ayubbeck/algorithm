class BM:
    def __init__(self):
        pass

    def get_bit(self, num, i):
        mask = 1 << i
        return num & mask

    def set_bit(self, num, i):
        mask = 1 << i
        return num | mask

    def clear_bit(self, num, i):
        mask = ~(1 << i)
        return num & mask

    def update_bit(self, num, i, bool_value):
        value = 1 if bool_value else 0
        mask = ~(1 << i)
        return (num & mask) | (value << i)
