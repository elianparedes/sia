from abc import ABC, abstractmethod

from src.classes.Gene import Gene

from src.classes.Genotipo import Genotipo


class MutationABC(ABC):

    """ Mutates a list of genes
    :return If None then no mutations. Else list of mutated genes
    """
    @classmethod
    @abstractmethod
    def mutate(cls, genes: Genotipo, probability: float) -> Genotipo | None:
        pass
