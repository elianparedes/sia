import math

from src.classes.characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class Content(CutoffABC):

    @classmethod
    def cutoff(cls, new_population: list, old_population: list[list[CharacterABC]], generation: int,
               cutoffparameter) -> bool:
        if not old_population or cutoffparameter > len(old_population):
            return False
        rango = len(old_population) - cutoffparameter

        for i in range(rango, len(old_population)):
            pop_max = max(new_population, key=lambda x: x.fitness()).fitness()
            if math.isclose(pop_max, max(old_population[i], key=lambda x: x.fitness()).fitness(),
                            rel_tol=1e-09) is False:
                return False

        return True
