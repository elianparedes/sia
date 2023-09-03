from src.selection.SelectionABC import SelectionABC
import random


class ProbabilisticTournament(SelectionABC):
    TOURNAMENT_SIZE = 2

    @classmethod
    def select(cls, population: [], individuals: int):

        if individuals <= 0:
            raise ValueError("Individuals must be greater than 0")

        new_population = []
        for i in range(individuals):
            threshold = random.uniform(0.5, 1)
            candidates = random.sample(population, cls.TOURNAMENT_SIZE)
            r_value = random.uniform(0, 1)
            if r_value < threshold:
                new_population.append(max(candidates))
            else:
                new_population.append(min(candidates))

        return new_population
