from src.classes.Genotype import Genotype
from src.replacement.ReplacementABC import ReplacementABC
from src.selection.SelectionABC import SelectionABC
from typing import List
from math import ceil, floor

class YoungBias(ReplacementABC):
    
    @classmethod
    def replace(cls, population: List[Genotype], children: List[Genotype], first_selection: SelectionABC , second_selection: SelectionABC, B: float = 0.5) -> List[Genotype]:
        n = len(population)
        k = len(children)

        if (k > n):
            return first_selection(children, ceil(n * B)) + second_selection(children, floor(n * (1 - B)))

        else:
            return children + first_selection(population, ceil((n - k) * B)) + second_selection(population, floor((n - k) * (1 - B)))

        