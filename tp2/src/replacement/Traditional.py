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

        first_selected_individuals = first_selection.select(new_population, ceil(n * B))
        remaining_individuals = [individual for individual in new_population if individual not in first_selected_individuals]
        second_selected_individuals = second_selection.select(remaining_individuals, floor(n * (1 - B)))

        return first_selected_individuals + second_selected_individuals
