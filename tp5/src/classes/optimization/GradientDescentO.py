import numpy as np

from src.classes.optimization.ConfigurableOptimizationABC import ConfigurableOptimizationABC


class GradientDescentO(ConfigurableOptimizationABC):
    @classmethod
    def calculate(cls, expected_value: float, activation_value: float, training_value: np.ndarray,
                  activation_derivative=None, excitement=None, **kwargs):
        """
        :param expected_value:
        :param activation_value:
        :param training_value:
        :param activation_derivative: taken from utils.Function.py
        :param excitement: ``excitement(training_value)``
        """
        return (cls.learning_rate * (expected_value - activation_value)
                * activation_derivative(excitement) * training_value)

    @classmethod
    def configure(cls, learning_rate: float, **kwargs):
        super().configure(learning_rate)
