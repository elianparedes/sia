from classes.NeuralNetwork import NeuralNetwork


class Extractor:
    @staticmethod
    def extract_latent_space(nn: NeuralNetwork):
        return nn.layers[(len(nn.layers) // 2)]
