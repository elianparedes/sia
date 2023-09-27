import numpy as np

from src.classes.optimization.ConfigurableOptimizationABC import ConfigurableOptimizationABC


class LinearO(ConfigurableOptimizationABC):

    @classmethod
    def calculate(cls, expected_value: float, activation_value: float, training_value: np.ndarray, **kwargs):
        return cls.learning_rate * (expected_value - activation_value) * training_value

    @classmethod
    def configure(cls, learning_rate: float, **kwargs):
        super().configure(learning_rate)
