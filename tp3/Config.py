import json
import os
from src.utils.Function import *

class ConfigUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    ACTIVATION_FUNCTIONS = {
        "sigmoid": SIGMOID,
        "tan_h": TAN_H,
        "relu": RELU,
    }

    ACTIVATION_FUNCTIONS_DERIVATIVES = {
        "sigmoid": SIGMOID_DERIVATIVE,
        "tan_h": TAN_H_DERIVATIVE,
        "relu": RELU_DERIVATIVE,
    }

class Config:

    def __init__(self, config_file):
        config_path = os.path.join(config_file)

        with open(config_path, "r") as f:
            config = json.load(f)

            multilayer_network_config = config['multilayer_network']
            self.architecture = multilayer_network_config['architecture']
            self.activation_functions = {
                "hidden_layers": ConfigUtils.ACTIVATION_FUNCTIONS[multilayer_network_config['activation_functions']['hidden_layers']],
                "output_layer": ConfigUtils.ACTIVATION_FUNCTIONS[multilayer_network_config['activation_functions']['output_layer']]
            }
            self.learning_rate = multilayer_network_config['learning_rate']
            
            training_config = multilayer_network_config['training']
            self.iterations = training_config['iterations']
            self.noise = training_config['noise']

            plot_config = config['plot']
            and_steps_config = plot_config['and_steps']
            xor_steps_config = plot_config['xor_steps']
            test_and_training_errors_config = plot_config['test_and_training_errors']

            self.plot = {
                'and_steps': {
                    'training_set': and_steps_config['training_set'],
                    'training_expected': and_steps_config['training_expected'],
                    'speed': and_steps_config['speed'],
                    'frame_duration': and_steps_config['frame_duration']
                },
                'xor_steps': {
                    'training_set': xor_steps_config['training_set'],
                    'training_expected': xor_steps_config['training_expected'],
                    'speed': xor_steps_config['speed'],
                    'frame_duration': xor_steps_config['frame_duration']
                },
                'test_and_training_errors': {
                    'epsilon': test_and_training_errors_config['epsilon'],
                    'learning_rate': test_and_training_errors_config['learning_rate'],
                    'bias': test_and_training_errors_config['bias'],
                    'max_epoch': test_and_training_errors_config['max_epoch']
                } 
               
            }
