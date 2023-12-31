import numpy as np


class Adam():

    def __init__(self, learning_rate=0.0001, b1=0.9, b2=0.999):
        self.learning_rate = learning_rate
        self.eps = 1e-8
        self.m = None
        self.v = None
        # Decay rates
        self.b1 = b1
        self.b2 = b2

    def calculate_delta_w(self, g, layer_input, epoch):
        # If not initialized
        if self.m is None:
            self.m = np.zeros(np.shape(g))
            self.v = np.zeros(np.shape(g))

        self.m = self.b1 * self.m + (1 - self.b1) * g
        self.v = self.b2 * self.v + (1 - self.b2) * np.power(g, 2)

        m = np.divide(self.m, 1 - self.b1 ** (epoch + 1))
        v = np.divide(self.v, 1 - self.b2 ** (epoch + 1))

        return -self.learning_rate * np.divide(m, (np.sqrt(v) + self.eps))
