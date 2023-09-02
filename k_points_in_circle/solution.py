from random import Random
from .point import Point
import numpy as np
import matplotlib.pyplot as plt
import math


def get_random_points(k: int, random: Random = None):
    random = Random() if random is None else random
    thetas = [random.uniform(0, 1) for _ in range(k)]
    rs = [random.uniform(0, 1) for _ in range(k)]
    points = [Point(rs[i], thetas[i] * 2 * np.pi) for i in range(k)]
    points[0].r, points[0].theta = 1, 0  # fix the first point at r:1, θ:0
    return points


class Solution:
    def __init__(self, n: int, random: Random, points: list = None):
        self.points = get_random_points(n, random) if points is None else points
        self.n = n
        self.fitness = None
        self.min_distances = None
        self.calc_distances()

    def calc_distances(self):
        min_distances = np.zeros(self.n)
        for i in range(self.n):
            point_i = self.points[i]
            min_distance_i = float('inf')
            for p in self.points:
                if p != point_i:
                    min_distance_i = min(min_distance_i, point_i.distance_square(p))
            min_distances[i] = min_distance_i

        self.min_distances = min_distances
        self.fitness = min(self.min_distances)

    def recombination(self, other: 'Solution', random: Random):
        weights = [self.fitness, other.fitness, (self.fitness + other.fitness) / 2]
        choices = random.choices(population=['self', 'other', 'avg'], weights=weights, k=self.n)
        points = []
        for i in range(self.n):
            choice = choices[i]
            if choice == 'self':
                points.append(self.points[i].copy())
            elif choice == 'other':
                points.append(other.points[i].copy())
            elif choice == 'avg':
                points.append(self.points[i].recombination(other.points[i]))

        return Solution(self.n, random, points)

    def mutate(self, r_sigma: float, theta_sigma: float, random: Random):
        # the more min-distance each point has, the lower probability for mutation it has
        weights = 1 - (self.min_distances / self.min_distances.sum())
        # make n/2 choices from 1 to n-1 (to avoid changing fixed point) according to weights
        choices = random.choices(population=range(1, self.n), weights=weights[1:], k=self.n // 2)
        for i in choices:
            p = self.points[i]
            p.r = (p.r + random.gauss(mu=0, sigma=r_sigma)) % 1
            p.theta = (p.theta + random.gauss(mu=0, sigma=theta_sigma)) % (2 * np.pi)

        self.calc_distances()

    #
    # ---------------------------------------------------------------
    # ---------------------------------------------------------------
    #

    def summery(self):
        s = '============== list of coordinates \n'
        for p in self.points:
            s += str(p) + '\n'
        s += '==============fitness \n'
        s += f'{math.sqrt(self.fitness):.6f} \n'
        s += '==============distances \n'
        distances = []
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                distances.append(self.points[i].distance_square(self.points[j]))
        distances.sort(reverse=True)
        for d in distances:
            s += f'{math.sqrt(d):.2f} \n'
        return s

    def plot(self, show=True, savefig=False):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))
        ax.set_ylim(0, 1)
        plt.suptitle(f"Solution for n = {self.n}, fitness: {math.sqrt(self.fitness):.6f}", fontsize=25)
        for p in self.points:
            plt.plot(p.theta, p.r, 'o', color='orange', markersize=10)
        if savefig:
            plt.savefig(f"outputs/solution-{self.n}.png")
        if show:
            plt.show()

    def __str__(self):
        return f'{self.n}-points, fitness: {self.fitness:.3f}'
