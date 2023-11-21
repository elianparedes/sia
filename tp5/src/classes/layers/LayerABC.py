from abc import ABC, abstractmethod


class LayerABC(ABC):

    # Calculates new neuron values (output) from a given input
    @abstractmethod
    def forward_propagation(self, input_data):
        pass

    @abstractmethod
    def forward_propagation_bias(self, input_data):
        pass

    # output_error: error array from previous layer
    @abstractmethod
    def backward_propagation(self, output_error, epoch):
        pass
    

    # wip auxiliar function that does not store calculated weights in the layer
    @abstractmethod
    def _backward_propagation(self, output_error):
        pass
    
    @abstractmethod
    def set_weights(self, weights_error, epoch):
        pass