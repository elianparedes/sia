class GradientDescent:

    def calculate_delta_w(self, weights_error, learning_rate, epoch):
        return learning_rate * weights_error
