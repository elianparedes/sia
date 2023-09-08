from abc import ABC

from src.classes.characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class Structure(CutoffABC, ABC):

    generations = 0

    @classmethod
    def set_generations(cls, generations):
        cls.generations = generations
    @classmethod
    def cutoff(cls, new_population: list, old_population: list[list[CharacterABC]], generation: int, cutoffparameter) -> bool:
        elementos_comunes = new_population
        if not old_population or cls.generations > len(old_population):
            return False
        population_len = len(new_population)
        rango = len(old_population) - cls.generations
        for i in range(rango, len(old_population)):
            elementos_comunes = list(filter(lambda x: x in elementos_comunes, old_population[i]))
            cantidad_elementos_comunes = len(elementos_comunes)
            if (cantidad_elementos_comunes / population_len) < cutoffparameter:
                return False
        return True

