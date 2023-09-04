from src.selection.SelectionABC import SelectionABC
import random


class DeterministicTournament(SelectionABC):

    tournament_size = None

    @classmethod
    def configure(cls, size=None, **kwargs):
        if size is not None:
            if size <= 0:
                raise ValueError("Size must be greater than 0")
            cls.tournament_size = size

    @classmethod
    def select(cls, population: [], individuals: int):
        if individuals <= 0:
            raise ValueError("Individuals must be greater than 0")

        if cls.tournament_size is None:
            raise ValueError("Tournament size not set. Please set it using 'configure' method.")

        new_population = []
        for i in range(individuals):
            tournament = random.sample(population, cls.tournament_size)
            individual = max(tournament)
            new_population.append(individual)

        return new_population
