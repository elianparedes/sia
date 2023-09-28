import json
import os
from src.utils.Function import *

class ConfigUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    ACTIVATION_FUNCTIONS = {
        "sigmoid": [SIGMOID, SIGMOID_DERIVATIVE],
        "tan_h": [TAN_H, TAN_H_DERIVATIVE],
        "relu": [RELU, RELU_DERIVATIVE],
    }

class Config:

    def __init__(self, config_file):
        config_path = os.path.join(config_file)

        with open(config_path, "r") as f:
            config = json.load(f)

            self.run = config['run']

            plot_config = config['plot']
            and_steps_config = plot_config['and_steps']
            xor_steps_config = plot_config['xor_steps']
            test_and_training_errors_config = plot_config['test_and_training_errors']
            split_ratio_errors_config = plot_config['split_ratio_errors']
            number_metrics_config = plot_config['number_metrics']

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
                    'max_epoch': test_and_training_errors_config['max_epoch'],
                    'batch_amount': test_and_training_errors_config['batch_amount'],
                    'activation_function': ConfigUtils.ACTIVATION_FUNCTIONS[test_and_training_errors_config['activation_function']],
                    'normalize_range': test_and_training_errors_config['normalize_range'],
                },
                'split_ratio_errors': {
                    'epsilon': split_ratio_errors_config['epsilon'],
                    'learning_rate': split_ratio_errors_config['learning_rate'],
                    'bias': split_ratio_errors_config['bias'],
                    'max_epoch': split_ratio_errors_config['max_epoch'],
                    'batch_amount': split_ratio_errors_config['batch_amount'],
                    'activation_function': ConfigUtils.ACTIVATION_FUNCTIONS[split_ratio_errors_config['activation_function']],
                    'normalize_range': split_ratio_errors_config['normalize_range'],
                },
                'number_metrics': {
                    'epsilon': number_metrics_config['epsilon'],
                    'learning_rate': number_metrics_config['learning_rate'],
                    'max_epoch': number_metrics_config['max_epoch'],
                    'batch_amount': number_metrics_config['batch_amount'],
                    'noise': number_metrics_config['noise']
                }
            }
