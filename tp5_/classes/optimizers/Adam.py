import numpy as np

from classes.optimizers import OptimizerABC

class Adam():

    def __init__(self, learning_rate=0.0001, b1=0.9, b2=0.999):
        self.learning_rate = learning_rate
        self.eps = 1e-8
        self.m = None
        self.v = None
        # Decay rates
        self.b1 = b1
        self.b2 = b2

    def calculate_delta_w(self, g: np.ndarray[float], layer_input, epoch):
        # If not initialized
        if self.m is None:
            self.m = np.zeros(np.shape(g))
            self.v = np.zeros(np.shape(g))

        self.m = self.b1 * self.m + (1 - self.b1) * g
        self.v = self.b2 * self.v + (1 - self.b2) * np.power(g, 2)
        m_hat = self.m / (1 - (self.b1 ** (epoch + 1)))
        v_hat = self.v / (1 - (self.b2 ** (epoch + 1)))

        toReturn = self.learning_rate * m_hat / (np.sqrt(v_hat) + self.eps)
        # print("toReturn", toReturn)
        return toReturn
