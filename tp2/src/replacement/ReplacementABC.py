from abc import ABC, abstractmethod

from src.selection.SelectionABC import SelectionABC
from src.classes.Genotype import Genotype
from typing import List

class ReplacementABC(ABC):

    @classmethod
    @abstractmethod
    def replace(cls, population: List[Genotype], children: List[Genotype], first_selection: SelectionABC , second_selection: SelectionABC, B: float = 0.5) -> List[Genotype]:
        pass
