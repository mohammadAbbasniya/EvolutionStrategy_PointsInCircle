from k_points_in_circle.evolution_strategy import NPointsES

if __name__ == '__main__':
    npes = NPointsES(n=7, population_size=20, max_iterations=10, random_state=0)
    solution = npes.run()

    print(solution.summery())
    solution.plot()

