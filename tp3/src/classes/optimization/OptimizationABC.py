from abc import ABC, abstractmethod

import numpy as np


class OptimizationABC(ABC):
    """ABC for optimization methods"""

    @classmethod
    @abstractmethod
    def calculate(cls, expected_value: float, activation_valule: float, training_value: np.ndarray, **kwargs):
        """Calculates ``delta w`` for the optimization method"""
        pass
