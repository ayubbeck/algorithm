import unittest
from jsm import Job

class JsmTests(unittest.TestCase):
    def setUp(self):
        self.jobs = ['j2', 'j1', 'j4', 'j3', 'j5']
        self.deadlines = {'j2':1, 'j1':2, 'j4':2, 'j3':3, 'j5':1}
        self.weights = {'j2':100, 'j1':60, 'j4':40, 'j3':20, 'j5':20}
        self.max_deadline = 3
        self.job = Job(self.jobs,
                       self.deadlines,
                       self.weights,
                       self.max_deadline)

    def test_scheduling(self):
        selected_jobs, profit = self.job.sequence()
        self.assertEqual(selected_jobs[0], 'j2')
        self.assertEqual(selected_jobs[1], 'j1')
        self.assertEqual(selected_jobs[2], 'j3')
        self.assertEqual(profit, 180)

if __name__ == "__main__":
    unittest.main()
