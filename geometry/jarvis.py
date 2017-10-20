class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ConvexHull:
    def __init__(self, points):
        self.hull = []
        self.points = points
        self.number_of_points = len(points)

    def orientation(self, p, q, r):
        # find the orientation
        val = ((q.y - p.y) * (r.x - q.x)) - ((q.x - p.x) * (r.y - q.y))
        # if it's then it's a straight line
        if val == 0:
            return 0
        # if larger than 0 then clockwise, otherwise counter clockwise
        return 1 if val > 0 else 2

    def preprocess_validation(self):
        # make sure there are more than 2 points
        if self.number_of_points < 3:
            return False
        return True

    def starting_point(self):
        # find the left most point
        # really the most lext X coordinate
        starting_index = 0
        for i in range(1, self.number_of_points):
            if self.points[i].x < self.points[starting_index].x:
                starting_index = i
        return starting_index

    def search(self, p):
        # compare points and find the next point in the hull
        r = (p + 1) % self.number_of_points
        for q in range(self.number_of_points):
            if self.orientation(self.points[p], self.points[q], self.points[r]) == 2:
                r = q
        return r

    def find(self):
        if self.preprocess_validation():
            l = self.starting_point()
            # starting point is in the hull
            self.hull.append(self.points[l])
            # search the next starting point
            p = self.search(l)
            while p != l:
                self.hull.append(self.points[p])
                p = self.search(p)
