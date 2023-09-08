from abc import ABC, abstractmethod

from src.classes.Genotype import Genotype


class MutationABC(ABC):

    """ Mutates a genotype
    :return If None then no mutations. Else mutated genotype
    """
    @classmethod
    @abstractmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        pass
