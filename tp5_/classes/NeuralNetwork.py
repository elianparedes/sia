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

    def predict(self, input_data):
        samples = len(input_data)
        result = []

        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

    def fit(self, x_train, y_train, epochs, learning_rate):
        samples = len(x_train)

        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                err += self.loss(y_train[j], output)

                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate, i)

            err /= samples
            print("error:", self.compute_error(x_train, y_train))


    def compute_error(self, dataset, expected):
        to_return = 0
        result = self.predict(dataset)[0]
        expected = expected[0]

    
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
