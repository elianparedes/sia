

class OjaAlgorithm:
    @staticmethod
    def train(network,input,initial_learning_rate):
        num_iterations = 100000
        for i in range(num_iterations):
            learning_rate = initial_learning_rate
            for register in input:
                activation = network.get_activation(register)
                network.update_weights(activation, learning_rate, register)
        return network
