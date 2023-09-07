from abc import ABC
from typing import List

from src.classes.Genotype import Genotype
from src.classes.characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class MaxGeneration(CutoffABC, ABC):

    @classmethod
    def cutoff(cls, population: List[CharacterABC],old_population: list[list[CharacterABC]], generation: int, cutoffparameter) -> bool:
        return generation >= cutoffparameter
