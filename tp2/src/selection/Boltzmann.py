import math
import random

from tp2.src.selection.SelectionABC import SelectionABC


class Boltzmann(SelectionABC):
    @classmethod
    def select(cls, population: [], individuals: int):
        new_population = []
        fitness_values = []
        population_len = len(population)
        temperature = 100
        generation = 10
        total = 0
        for individual in population:
            local_value = math.exp(individual.fitness() / temperature)
            fitness_values.append(local_value)
            total += local_value
        total = total / population_len
        for i in range(population_len):
            fitness_values[i] = fitness_values[i] / total

        for _ in range(individuals):
            selected_individual = random.choices(population, weights=fitness_values, k=1)[0]
            index = population.index(selected_individual)
            population.pop(index)
            fitness_values.pop(index)
            new_population.append(selected_individual)
        return new_population
