from abc import ABC, abstractmethod
from typing import List

import Genotype
from characters.CharacterABC import CharacterABC


class CutoffABC(ABC):

    @classmethod
    @abstractmethod
    def cutoff(cls, population: List[CharacterABC], old_population: list[list[CharacterABC]], generation: int, cutoffparameter) -> bool:
        pass