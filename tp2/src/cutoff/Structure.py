from abc import ABC

from Genotype import Genotype
from characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class Structure(CutoffABC, ABC):

    @classmethod
    def cutoff(cls, new_population: list, old_population: list[list[CharacterABC]], generation: int, cutoffparameter) -> bool:
        elementos_comunes = new_population
        if cutoffparameter > len(old_population):
            rango = 0
        else:
            rango = len(old_population) - cutoffparameter
        for i in range(rango, len(old_population)):
            elementos_comunes = list(filter(lambda x: x in elementos_comunes, old_population[i]))
            cantidad_elementos_comunes = len(elementos_comunes)
            if cantidad_elementos_comunes < cutoffparameter:
                return False
        return True

