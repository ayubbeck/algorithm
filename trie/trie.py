class Node(object):
    def __init__(self, data):
        self.data = data
        self.child = {}
        self.end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = Node('root')

    def insert(self, word):
        node = self.root
        for char in list(word):
            if char not in node.child:
                node.child[char] = Node(char)
            node = node.child[char]
        node.end_of_word = True

    def query(self, word):
        node = self.root
        for char in list(word):
            if char not in node.child:
                return False
            node = node.child[char]
        if node.end_of_word:
            return True
        return False

    def prefixes(self, word):
        if not self.query(word):
            return []
        prefix = ''
        node = self.root
        prefixes = []
        for char in list(word):
            prefix += char
            node = node.child[char]
            if node.end_of_word and prefix != word:
                prefixes.append(prefix)
        return prefixes
