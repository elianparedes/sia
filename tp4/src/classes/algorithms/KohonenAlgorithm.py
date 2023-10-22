class KohonenAlgorithm:
    @staticmethod
    def train(network, training_set, initial_learning_rate, initial_radius):
        num_iterations = 1000 * network.neuron_qty
        learning_rate_schedule = [initial_learning_rate / (i + 1) for i in range(num_iterations)]
        radius_schedule = [(num_iterations - i) * initial_radius / num_iterations for i in range(num_iterations)]
        for i in range(num_iterations):
            learning_rate = learning_rate_schedule[i]
            radius = radius_schedule[i]
            if radius < 1:
                radius = 1

            for register in training_set:
                winner_neuron, _ = network.get_winner_neuron(register)

                neighbours = network.get_neighbours(winner_neuron.x, winner_neuron.y, radius)
                for neighbour in neighbours:
                    neighbour.set_weights(network.kohonen_rule(neighbour, register, learning_rate))

        return network

