import numpy as np

from src.classes.optimization.ConfigurableOptimizationABC import ConfigurableOptimizationABC
from src.classes.optimization.GradientDescentO import GradientDescentO


class MomentumO(ConfigurableOptimizationABC):
    momentum_coefficient = None

    @classmethod
    def calculate(cls, expected_value: float, activation_value: float, training_value: np.ndarray,
                  activation_derivative=None, excitement=None, prev_delta_w=0, **kwargs):
        return (cls.learning_rate * (expected_value - activation_value) * activation_derivative(excitement) * training_value
                + cls.momentum_coefficient * 0)

    @classmethod
    def configure(cls, learning_rate: float, momentum_coefficient: float = None, **kwargs):
        super().configure(learning_rate)
        if momentum_coefficient is not None:
            cls.momentum_coefficient = momentum_coefficient
