import math
import random

from tp2.src.selection.SelectionABC import SelectionABC


#TODO implement generation
#TODO get constants from config file
class Boltzmann(SelectionABC):
    @classmethod
    def select(cls, population: [], individuals: int):
        new_population = []
        fitness_values = []
        population_len = len(population)
        generation = 10

        t0 = 100
        tc = 50
        k = 0.1
        temperature = tc + (t0 + tc) * math.exp(-k * generation)

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
