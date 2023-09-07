from src.classes.Genotype import Genotype
from src.replacement.ReplacementABC import ReplacementABC
from src.selection.SelectionABC import SelectionABC
from typing import List
from math import ceil, floor


class Traditional(ReplacementABC):

    @classmethod
    def replace(cls, population: List[Genotype], children: List[Genotype], first_selection: SelectionABC,
                second_selection: SelectionABC, B: float = 0.5) -> List[Genotype]:
        n = len(population)

        new_population = population + children

        return first_selection.select(new_population, ceil(n * B)) + second_selection.select(new_population,
                                                                                             floor(n * (1 - B)))
