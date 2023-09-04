from src.selection.SelectionABC import SelectionABC
import random


class Roulette(SelectionABC):

    @classmethod
    def select(cls, population: [], individuals: int):
        new_population = []
        fitness_values = []
        population_len = len(population)
        relatives = [0] * population_len
        cumulative = [0] * population_len

        for individual in population:
            fitness_values.append(individual.fitness())
        fitness_total = sum(fitness_values)

        for i in range(population_len):
            relatives[i] = fitness_values[i] / fitness_total
            cumulative[i] = relatives[i]
            if i != 0:
                cumulative[i] += cumulative[i - 1]

        for j in range(individuals):
            random_number = random.uniform(0, 1)
            for k in range(population_len):
                if k == population_len:
                    new_population.append(population[k])
                    break
                if random_number <= cumulative[k]:
                    if k == 0 or k != 0 and cumulative[k-1] < random_number:
                        new_population.append(population[k])
                        break

        return new_population
