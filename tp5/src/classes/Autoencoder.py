from src.classes.NeuralNetwork import NeuralNetwork


class Autoencoder(NeuralNetwork):

    def __init__(self, latent_space_idx ,architecture, hidden_function, hidden_derivative, output_function, output_derivative,
                 learning_rate=0.01, weight_distribution=(-1, 1), weights=None):
        super().__init__(architecture,hidden_function, hidden_derivative, output_function, output_derivative,learning_rate,weight_distribution, weights)
        self.latent_space_index = latent_space_idx

    def get_latent_space_input(self, dataset):
        new_input = dataset
        for i in range(0,self.latent_space_index):
            new_input = self.layers[i].test_activation(new_input)
        return new_input
