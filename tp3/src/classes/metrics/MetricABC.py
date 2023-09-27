from abc import ABC, abstractmethod


class MetricABC(ABC):

    @classmethod
    @abstractmethod
    def calculate(cls, true_positive, true_negative, false_positive, false_negative):
        pass


