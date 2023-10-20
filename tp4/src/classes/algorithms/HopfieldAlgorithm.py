
class HopfieldAlgorithm:
    @staticmethod
    def train(network, epochs):
        for _ in range(epochs):
            network.train_epoch()
        return network
