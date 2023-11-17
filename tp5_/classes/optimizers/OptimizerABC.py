from abc import ABC


class OptimizerABC(ABC):

    def calculate_delta_w(self, output_error, layer_input, weights,epoch):
        pass