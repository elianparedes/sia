import json
import os

from src.classes.Genotype import Genotype


class Config:

    def __init__(self, config_file):
        config_path = os.path.join(config_file)

        with open(config_path, "r") as f:
            config = json.load(f)
            self.character = config['character']
            self.crossover = config['crossover']
            self.mutation = config['mutation']
            self.selection = config['selection']
            self.cutoff = config['cutoff']
            self.genotypes = []
            for genotype in config['seed']:
                self.genotypes.append(Genotype(genotype["strength"], genotype["agility"], genotype["skill"], genotype["endurance"], genotype["health"],
                                               genotype["height"]))
