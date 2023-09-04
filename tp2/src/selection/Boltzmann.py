import math
import random

from src.selection.SelectionABC import SelectionABC


# TODO implement generation
# TODO get constants from config file
class Boltzmann(SelectionABC):
    T0 = 0
    TC = 0
    K = 0
    generation = 0

    @classmethod
    def set_T0(cls, t0: float):
        if t0 <= 0:
            raise ValueError("Size must be greater than 0")
        cls.T0 = t0
    @classmethod
    def set_TC(cls, tc: float):
        if tc <= 0:
            raise ValueError("Size must be greater than 0")
        cls.TC = tc
    @classmethod
    def set_K(cls, k: float):
        if k <= 0:
            raise ValueError("Size must be greater than 0")
        cls.K = k
    @classmethod
    def set_generation(cls, generation: int):
        if generation <= 0:
            raise ValueError("Size must be greater than 0")
        cls.generation = generation

    @classmethod
    def select(cls, population: [], individuals: int):
        if individuals <= 0 or cls.T0 <= 0 or cls.TC <= 0 or cls.K <= 0 or cls.generation <= 0:
            raise ValueError("Individuals must be greater than 0")
        new_population = []
        fitness_values = []
        population_len = len(population)

        temperature = cls.TC + (cls.T0 + cls.TC) * math.exp(-cls.K * cls.generation)

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
