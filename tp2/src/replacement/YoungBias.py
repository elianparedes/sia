from src.classes.Genotype import Genotype
from src.replacement.ReplacementABC import ReplacementABC
from src.selection.SelectionABC import SelectionABC
from typing import List
from math import ceil, floor


class YoungBias(ReplacementABC):

    @classmethod
    def replace(cls, population: List[Genotype], children: List[Genotype], first_selection: SelectionABC,
                second_selection: SelectionABC, B: float = 0.5) -> List[Genotype]:
        n = len(population)
        k = len(children)

        if k > n:
            first_selected_children = first_selection.select(children, ceil(n * B))
            remaining_children = [child for child in children if child not in first_selected_children]
            second_selected_children = second_selection.select(remaining_children, floor(n * (1 - B)))

            return first_selected_children + second_selected_children
        
        else:
            first_selected_individuals = first_selection.select(population, ceil((n - k) * B)) 
            remaining_individuals = [individual for individual in population if individual not in first_selected_individuals]
            second_selected_individuals = second_selection.select(remaining_individuals, floor((n - k) * (1 - B)))
            
            return children + first_selected_individuals + second_selected_individuals
