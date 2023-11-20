class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        self.layers.append(layer)

    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    def feed_forward(self, data):
        input = data
        for layer in self.layers:
            input = layer.forward_propagation(input)
        return input

    def backpropagation(self, error):
        gradients = []
        last_delta = error
        output_error_last = None
        for layer in reversed(self.layers):
            input_error, weights_error, output_error = layer._backward_propagation(last_delta)
            last_delta = input_error
            output_error_last = output_error
            gradients.append(weights_error)
        gradients.reverse()
        return gradients, output_error_last

    def update_weights(self, gradients, epoch):
        for i in range(len(self.layers)):
            self.layers[i].set_weights(gradients[i], epoch)


    def predict(self, input_data):
        input_data = [input_data]
        samples = len(input_data)
        result = []
        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        return result

    def fit(self, training_set, test_set, epochs, learning_rate, training_expected, test_expected):
        samples = len(training_set)
        computed_error = None

        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = training_set[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                err += self.loss(training_expected[j], output)

                error = self.loss_prime(training_expected[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, i)

            err /= samples
            computed_error = self.compute_error(test_set, test_expected)
            print("error: ", computed_error)

            if computed_error <= 1:
                break

    def compute_error(self, dataset, expected):
        to_return = 0
        result = self.predict(dataset)[0]
        expected = expected
        for i in range(0, len(result)):
            # result[i] = (result[i] + 1) / 2
            result[i] = result[i].round().astype(int)

            errors = 0
            for j in range(0, len(result[i])):
                if result[i][j] != expected[i][j]:
                    errors += 1

            if errors > to_return:
                to_return = errors

        return to_return
