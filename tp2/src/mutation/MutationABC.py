from abc import ABC, abstractmethod

from src.classes.Gene import Gene


class MutationABC(ABC):

    """ Mutates a list of genes
    :return If None then no mutations. Else list of mutated genes
    """
    @classmethod
    @abstractmethod
    def mutate(cls, genes: list[Gene], probability: float) -> list[Gene] | None:
        pass
