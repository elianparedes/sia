from abc import ABC, abstractmethod

from src.classes.Genotype import Genotype


class CrossoverABC(ABC):

    """ Crosses 2 genes
    :return tuple[Gene, Gene] containing the genes of the 2 children
    """
    @classmethod
    @abstractmethod
    def cross(cls, gene1: Genotype, gene2: Genotype) -> tuple[Genotype, Genotype]:
        pass
