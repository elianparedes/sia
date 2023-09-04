from abc import ABC, abstractmethod

from src.classes.Genotype import Genotype


class MutationABC(ABC):

    """ Mutates a list of genes
    :return If None then no mutations. Else list of mutated genes
    """
    @classmethod
    @abstractmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        pass
