from .solution import Solution
import numpy as np
from random import Random


class NPointsES:
    def __init__(self, n, population_size, max_iterations, random_state):
        self.n = n
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.random = Random(random_state)

    def run(self):
        population = [Solution(self.n, self.random) for _ in range(self.population_size)]
        best_solution = population[0]
        iteration = 0
        r_sigma = 1
        theta_sigma = np.pi
        r_sigma_reducer = r_sigma / self.max_iterations
        theta_sigma_reducer = theta_sigma / self.max_iterations

        while iteration < self.max_iterations:
            # ----------------- recombination parents according to their fitness
            # population :      [ S1, S2, S3 ,..., Sn ]
            # new_population :  [ S1 recombine with Sn,
            #                     S2 recombine with S1,
            #                     S3 recombine with S2,
            #                     ...
            #                     Sn recombine with Sn-1 ]
            new_population = []
            for i in range(self.population_size):
                new_population.append(population[i].recombination(population[i - 1], self.random))

            # ----------------- mutate recombined population
            for p in new_population:
                p.mutate(r_sigma, theta_sigma, self.random)

            # ----------------- prepare new generation
            population = population[:int(self.population_size * 0.6)]  # kick out bottom 40% of population
            population.extend(new_population)  # attach new population to remaining (top 60%)

            # sort population according to their fitness (higher fitness come first)
            population.sort(key=lambda s: s.fitness, reverse=True)
            # pick top performing solutions
            population = population[:self.population_size]

            # update best_solution if there is a better one
            if best_solution.fitness < population[0].fitness:
                best_solution = population[0]

            # ----------------- update parameters
            # todo: another way to decrease sigma is f(x) = M -  (x / L)^3  × M
            #  where M = starting point and L = max iterations
            r_sigma -= r_sigma_reducer
            theta_sigma -= theta_sigma_reducer
            iteration += 1

        return best_solution

