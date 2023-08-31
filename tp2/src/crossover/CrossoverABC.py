from abc import ABC, abstractmethod

from src.classes.Gene import Gene


class CrossoverABC(ABC):

    """ Crosses 2 genes
    :return tuple[Gene, Gene] containing the genes of the 2 children
    """
    @classmethod
    @abstractmethod
    def cross(cls, gene1: Gene, gene2: Gene) -> tuple[Gene, Gene]:
        pass
