import numpy as np


class OjaAlgorithm:
    @staticmethod
    def train(network,input,initial_learning_rate,epochs):
        num_iterations = epochs
        for i in range(num_iterations):
            learning_rate = initial_learning_rate
            for register in input:
                activation = network.get_activation(register)
                network.update_weights(activation, learning_rate, register)
        return network
    @staticmethod
    def pc1(oja_network, input):
        pc1 = []
        for row in input:
            y_value1 = np.dot(-1 * oja_network.neurons.get_weights(), row)
            pc1.append(y_value1)
        return pc1
    @staticmethod
    def error(oja_network, input, pc1_input):
        pc1 = OjaAlgorithm.pc1(oja_network, input)
        error = 0
        for i in range(len(pc1)):
            error += np.linalg.norm(pc1[i] - pc1_input[i])
        return error