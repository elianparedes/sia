from src.classes.Genotype import Genotype
from src.classes.characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class Content(CutoffABC):

    @classmethod
    def cutoff(cls, new_population: list, old_population:list[list[CharacterABC]],generation: int, cutoffparameter) -> bool:
        if cutoffparameter > len(old_population):
            rango = 0
        else:
            rango = len(old_population) - cutoffparameter

        for i in range(rango, len(old_population)):
            pop_max = max(new_population, key=lambda x: x.fitness())
            if pop_max != max(old_population[i], key=lambda x: x.fitness()):
                return False
        return True
