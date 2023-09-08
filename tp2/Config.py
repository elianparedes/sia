import json
import os

from src.classes.Genotype import Genotype
from src.selection.SelectionFactory import SelectionFactory
from src.utils.ConfigUtils import ConfigUtils


class Config:

    def __init__(self, config_file, seed=None):
        config_path = os.path.join(config_file)

        with open(config_path, "r") as f:
            config = json.load(f)
            self.character = ConfigUtils.CHARACTERS[config['character']]
            self.crossover = ConfigUtils.CROSSOVER[config['crossover']]
            self.mutation = ConfigUtils.MUTATION[config['mutation']['type']]
            self.mutation_probability = config['mutation']['probability']

            self.first_selection = SelectionFactory.configure(config['selection']['first-selection']['type'],
                                                              **config['selection']['first-selection']['parameters'])
            self.second_selection = SelectionFactory.configure(config['selection']['second-selection']['type'],
                                                               **config['selection']['second-selection']['parameters'])

            self.a_value = config['selection']['a-value']
            self.individuals = config['selection']['individuals']

            self.replacement_type = ConfigUtils.REPLACEMENT[config['replacement']['type']]
            self.replacement_first_selection = SelectionFactory.configure(
                config['replacement']['first-selection']['type'],
                **config['replacement']['first-selection']['parameters'])
            self.replacement_second_selection = SelectionFactory.configure(
                config['replacement']['second-selection']['type'],
                **config['replacement']['second-selection']['parameters'])

            self.b_value = config['replacement']['b-value']

            self.cutoff = ConfigUtils.CUTOFF[config['cutoff']['type']]
            if config['cutoff']['type'] == "structure":
                self.cutoff.set_generations(config['cutoff']['generations'])
            self.cutoff_parameter = config['cutoff']['parameter']

            if seed is not None:
                self.genotypes = seed
            else:  # seed is none so we want to generate it from the cofig file
                self.genotypes = []
                for genotype in config['seed']:
                    self.genotypes.append(
                        Genotype(genotype["strength"], genotype["agility"], genotype["skill"], genotype["endurance"],
                                 genotype["health"],
                                 genotype["height"]))
