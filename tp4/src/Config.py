import json
import os

from src.classes.similarity.Euclidean import Euclidean
from src.classes.similarity.Exponential import Exponential
from src.classes.weights.Random import Random
from src.classes.weights.SetBased import SetBased

# Plot field names
CONFIG_MAP = {
    "similarity": {
        "euclidean": Euclidean,
        "exponential": Exponential
    },
    "weight_initializer": {
        "random": Random,
        "set_based": SetBased
    }
}

class Config:
    def __init__(self, config_file):

        config_path = os.path.join(os.path.dirname(__file__), config_file)

        with open(config_path, "r") as f:
            config = json.load(f)

            self.run = config['run']

            algorithm_config = config['algorithms']
            kohonen_config = algorithm_config['kohonen']
            plot_config = config['plots']

            self.algorithms = {
                'kohonen': {
                    'neuron_qty': kohonen_config['neuron_qty'],
                    'similarity': CONFIG_MAP['similarity'][kohonen_config['similarity']],
                    'weight_initializer': CONFIG_MAP['weight_initializer'][kohonen_config['weight_initializer']],
                    'radius': kohonen_config['radius'],
                    'learning_rate': kohonen_config['learning_rate'],
                }
            }

            self.plots = {
                'letters': {
                    'training_letters': plot_config['letters']['training_letters'],
                    'input': plot_config['letters']['input'],
                    'max_epochs': plot_config['letters']['max_epochs'],
                    'noise': plot_config['letters']['noise'],
                },
                'big_letters': {
                    'training_letters': plot_config['big_letters']['training_letters'],
                    'input': plot_config['big_letters']['input'],
                    'max_epochs': plot_config['big_letters']['max_epochs'],
                    'noise': plot_config['big_letters']['noise'],
                }
            }
