import random
from abc import ABC, abstractmethod


class StatABC(ABC):

    @abstractmethod
    def mutate(self):
        pass
