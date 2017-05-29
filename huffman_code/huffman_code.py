import Queue as Q

class Char:
    '''
        Both leaf and inner nodes on the huffman tree use this node class
    '''
    def __init__(self, char = None, freq = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    '''
        Compare two items of Priority Queue on frequency
    '''
    def __cmp__(self, other):
        return cmp(self.freq, other.freq)

    def __str__(self):
        return str(self.char) + ' ' + str(self.freq)

class HuffmanCode:
    def __init__(self, q, size):
        self.q = q # prioritized queue
        self.size = size
        self.code_dict = {} # dictionaty for codes

    '''
         Generate Huffman tree
         Basically, putting the least used chars on the bottom of the tree and
         most used chars on the heigher part of the tree.
    '''
    def generate_tree(self):
        for i in range(self.size - 1):
            temp = Char()
            min_one = self.q.get()
            min_two = self.q.get()
            temp.left = min_one
            temp.right = min_two
            temp.freq = min_one.freq + min_two.freq
            self.q.put(temp)

        return self.q.get()

    '''
        Generate code for each letters that the file of text has.
        Traversing the tree in pre order fashion
    '''
    def generate_code(self, node, code):
        if node.char is not None:
            self.code_dict[node.char] = code
        if node.left is not None:
            self.generate_code(node.left, code + '0')
        if node.right is not None:
            self.generate_code(node.right, code + '1')

    '''
        Finally, everything is done! all we have to here is
        to itereate through the text and encode the chars
    '''
    def encode(self, str):
        encoded_str = ''
        for i in list(str):
            encoded_str += self.code_dict[i]

        return encoded_str

class Prioritize:
    '''
        This class prioritizes given text and stores the
        chars and their freqs in Priority Queue
    '''
    def __init__(self, str):
        self.char_freq = self.process(str)
        self.size = len(self.char_freq)
        self.q = self.prioritize()

    '''
        Split the text and create return a dict
        with chars and their freqs
    '''
    def process(self, str):
        dict = {}
        for i in list(str):
            if dict.has_key(i):
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        return dict

    '''
        Loop thru the char dict/freq and create a Priority Queue
    '''
    def prioritize(self):
        q = Q.PriorityQueue()
        for i in self.char_freq.keys():
            q.put(Char(i, self.char_freq[i]))
        return q
