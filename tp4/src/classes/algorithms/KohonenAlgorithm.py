class KohonenAlgorithm:
    @staticmethod
    def train(network, training_set, learning_rate, radius):
        for i in range(400 * network.neuron_qty):
            for register in training_set:
                winner_neuron, _ = network.get_winner_neuron(register)
                radius = (400 * network.neuron_qty - i) * radius / (400 * network.neuron_qty)
                if radius < 1:
                    radius = 1
                neighbours = network.get_neighbours(winner_neuron.x, winner_neuron.y, radius)
                for neighbour in neighbours:
                    neighbour.set_weights(network.kohonen_rule(neighbour, register, learning_rate))

        return network
