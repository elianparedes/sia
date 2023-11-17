import numpy as np

class GradientDescent:

    def calculate_delta_w(self, weights_error, learning_rate):
        return learning_rate * weights_error