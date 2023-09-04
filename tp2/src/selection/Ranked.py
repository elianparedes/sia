from src.selection.SelectionABC import SelectionABC
import random


class Ranked(SelectionABC):

    @classmethod
    def select(cls, population: [], individuals: int):
        new_population = []
        population_len = len(population)
        ranked_population = sorted(population, key=lambda individual: individual.fitness(), reverse=True)

        selection_weights = [((population_len - (i + 1)) / population_len) for i in range(population_len)]

        for _ in range(individuals):
            selected_individual = random.choices(ranked_population, weights=selection_weights, k=1)[0]
            new_population.append(selected_individual)

        return new_population
