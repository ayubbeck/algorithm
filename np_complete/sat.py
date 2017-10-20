import random

'''
    Certificate and Verifier for NP hard 3-SAT problem.
    P = problems solved in polynomial time
    NP = problems solved in non deterministic polynomial time
    NP Complete = as hard as NP problem
'''
class SAT:
    def __init__(self):
        self.cert_size = 6
        self.cert = [bool(random.getrandbits(1)) for i in range(self.cert_size)]

    def verify(self):
        return (self.cert[0] or self.cert[1] or self.cert[2]) and (self.cert[3] or self.cert[4] or self.cert[5])
