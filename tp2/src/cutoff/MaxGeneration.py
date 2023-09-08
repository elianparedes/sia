from typing import List

from src.classes.characters.CharacterABC import CharacterABC
from src.cutoff.CutoffABC import CutoffABC


class MaxGeneration(CutoffABC):

    @classmethod
    def cutoff(cls, population: List[CharacterABC], old_population: list[list[CharacterABC]], generation: int,
               cutoffparameter) -> bool:
        return generation >= cutoffparameter
