from src.classes.characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class OptimumEnviroment(CutoffABC):

    @classmethod
    def cutoff(cls, population: list[CharacterABC], old_population: list[list[CharacterABC]], generation: int,
               cutoffparameter) -> bool:
        return max(population, key=lambda x: x.fitness()).fitness() >= cutoffparameter
