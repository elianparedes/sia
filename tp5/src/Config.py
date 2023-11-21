import json
import os

from src.classes.functions.ActivationFunctions import SIGMOID
from src.classes.functions.ActivationFunctions import SIGMOID_DERIVATIVE

from src.classes.functions.ActivationFunctions import TAN_H
from src.classes.functions.ActivationFunctions import TAN_H_DERIVATIVE

from src.classes.functions.ActivationFunctions import RELU
from src.classes.functions.ActivationFunctions import RELU_DERIVATIVE

from src.classes.functions.NoiseFunctions import salt_and_pepper
from src.classes.functions.NoiseFunctions import gaussian_noise

FUNCTIONS_MAPS = {
    "SIGMOID": [SIGMOID, SIGMOID_DERIVATIVE],
    "TAN_H": [TAN_H, TAN_H_DERIVATIVE],
    "RELU": [RELU, RELU_DERIVATIVE]
}

DEFAULT_FUNCTION = FUNCTIONS_MAPS["TAN_H"]

NOISE_FUNCTIONS = {
    "SALT_AND_PEPPER": salt_and_pepper,
    "GAUSSIAN_NOISE": gaussian_noise
}

DEFAULT_NOISE_FUNCTION = gaussian_noise
DEFAULT_NOISE_PARAMS = {
    "mean": 0,
    "std_deviation": 0.5
}


class Config:

    def __init__(self, config_file):
        config_path = os.path.join(os.path.dirname(__file__), config_file)

        with open(config_path, "r") as f:
            config = json.load(f)

            self.run = config['run']
            self.save_dataframe = config['save_dataframe']
            self.load_dataframe = config['load_dataframe']

            config_autoencoder = config['autoencoder']
            config_denoising = config['denoising']
            config_vae = config['vae']

            self.autoencoder = {
                "layers": config_autoencoder['layers'],
                "activation": FUNCTIONS_MAPS.get(config_autoencoder['activation'][0], DEFAULT_FUNCTION[0]),
                "activation_prime": FUNCTIONS_MAPS.get(config_autoencoder['activation'][1], DEFAULT_FUNCTION[1]),
                "epochs": config_autoencoder['epochs'],
                "learning_rate": config_autoencoder['learning_rate'],
                "batch_size": config_autoencoder['batch_size']
            }

            self.denoising = {
                "layers": config_denoising['layers'],
                "activation": FUNCTIONS_MAPS.get(config_autoencoder['activation'][0], DEFAULT_FUNCTION[0]),
                "activation_prime": FUNCTIONS_MAPS.get(config_autoencoder['activation'][1], DEFAULT_FUNCTION[1]),
                "epochs": config_denoising['epochs'],
                "learning_rate": config_denoising['learning_rate'],
                "batch_size": config_denoising['batch_size'],
                "noise_function": NOISE_FUNCTIONS.get(config_denoising['noise_function'], DEFAULT_NOISE_FUNCTION),
                "noise_function_params": config_denoising.get(config_denoising['noise_function'].lower(),
                                                              DEFAULT_NOISE_PARAMS)
            }

            self.vae = {
                "encoder": {
                    "layers": config_vae['encoder']['layers'],
                    "activation": FUNCTIONS_MAPS.get(config_autoencoder['activation'][0], DEFAULT_FUNCTION[0]),
                    "activation_prime": FUNCTIONS_MAPS.get(config_autoencoder['activation'][1], DEFAULT_FUNCTION[1]),
                },
                "decoder": {
                    "layers": config_vae['decoder']['layers'],
                    "activation": FUNCTIONS_MAPS.get(config_autoencoder['activation'][0], DEFAULT_FUNCTION[0]),
                    "activation_prime": FUNCTIONS_MAPS.get(config_autoencoder['activation'][1], DEFAULT_FUNCTION[1]),
                },
                "epochs": config_vae['epochs'],
                "learning_rate": config_vae['learning_rate'],
            }
