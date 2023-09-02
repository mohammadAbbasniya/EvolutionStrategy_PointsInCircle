import numpy as np


class Point:
    def __init__(self, r, theta):
        self.theta = theta
        self.r = r

    def distance_square(self, other):
        r1, r2 = self.r, other.r
        return r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * np.cos(self.theta - other.theta)

    def recombination(self, other: 'Point'):
        r = (self.r + other.r) / 2
        theta = (self.theta + other.theta) / 2
        return Point(r, theta)

    def __str__(self):
        return f"r:{self.r:.6f}  θ:{self.theta:.6f}"

    def copy(self):
        return Point(r=self.r, theta=self.theta)
