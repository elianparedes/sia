import numpy as np
class ADAM:

    def __init__(self, b1, b2, e, a, x_dimension, y_dimension):
        self.b1 = b1
        self.b2 = b2
        self.e = e
        self.a = a

        self.m = np.zeros([x_dimension, y_dimension])
        self.v = np.zeros([x_dimension, y_dimension])
        self.t = 0

    def optimize(self, g):
        self.t += 1
        new_m = self.b1 * self.m + (1 - self.b1) * g
        new_v = self.b2 * self.v + (1 - self.b2) * np.power(g, 2)
        m_hat = new_m / (1 - self.b1 ** self.t)
        v_hat = new_v / (1 - self.b2 ** self.t)
        self.m = new_m.copy()
        self.v = new_v.copy()
        return self.a * m_hat / (np.sqrt(v_hat) + self.e)
