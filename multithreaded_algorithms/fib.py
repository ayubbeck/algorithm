import threading
from Queue import Queue

class Fibonacci:
    def __init__(self, sequence):
        self.q = Queue()
        self.fib = self.fib(self.q, sequence)

    def fib(self, q, n):
        if n <= 2:
            q.put(n)
        else:
            x = threading.Thread(name='fib', target=self.fib, args=(q, n - 1))
            y = threading.Thread(name='fib', target=self.fib, args=(q, n - 2))
            x.start()
            y.start()
            x.join()
            y.join()
            q.put(q.get() + q.get())
