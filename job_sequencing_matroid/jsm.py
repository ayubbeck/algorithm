
class Job:
    def __init__(self, jobs, deadlines, weights, max_deadline):
        self.jobs = jobs
        self.deadlines = deadlines
        self.weights = weights
        self.max_deadline = max_deadline
        self.time_slots = [None for i in range(max_deadline)]

    '''
        takes O(n^2), uses greedy approach to
        get the max profit
    '''
    def sequence(self):
        profit = 0
        for job in self.jobs:
            deadline = self.deadlines[job]
            if deadline <= self.max_deadline:
                while deadline != 0:
                    if self.time_slots[deadline - 1] is None:
                        self.time_slots[deadline - 1] = job
                        profit += self.weights[job]
                        deadline = 0
                    else:
                        deadline -= deadline
        return self.time_slots, profit
