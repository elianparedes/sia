from abc import ABC, abstractmethod

from src.selection.SelectionABC import SelectionABC


class ConfigurableSelectionABC(SelectionABC, ABC):

    @classmethod
    @abstractmethod
    def configure(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def select(cls, population: [], individuals: int):
        pass
