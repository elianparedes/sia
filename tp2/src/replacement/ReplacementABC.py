from abc import ABC, abstractmethod

from src.selection.SelectionABC import SelectionABC
from src.classes.Genotype import Genotype
from typing import List

class ReplacementABC(ABC):

    """Replaces 100*B% population with first selection and 100*(1-B)% with the second selection
    :param  population Population to be replaced
    :param  children Used to replace all/some of the population (depends on method)
    :param  first_selection Selection method which will select 100*B% of the population
    :param  second_selection Selection method which will select 100*(1-B)% of the population
    :param  B Ratio of the population to be replaced by first_selection

    :returns List of the genotypes of the new population
    """
    @classmethod
    @abstractmethod
    def replace(cls, population: List[Genotype], children: List[Genotype], first_selection: SelectionABC,
                second_selection: SelectionABC, B: float = 0.5) -> List[Genotype]:
        pass
