from abc import abstractmethod

import numpy as np

from src.classes.optimization.OptimizationABC import OptimizationABC


class ConfigurableOptimizationABC(OptimizationABC):
    """ABC to add fixed parameters from the outside, independent to any class"""
    learning_rate = None

    @classmethod
    @abstractmethod
    def calculate(cls, expected_value: float, activation_valule: float, training_value: np.ndarray, **kwargs):
        pass

    @classmethod
    def configure(cls, learning_rate: float, **kwargs):
        if learning_rate is None:
            raise ValueError("Missing learning rate")
        cls.learning_rate = learning_rate
        pass

