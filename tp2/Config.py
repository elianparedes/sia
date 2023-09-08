import json
import os

from src.classes.Genotype import Genotype

from src.classes.characters.Archer import Archer
from src.classes.characters.Defender import Defender
from src.classes.characters.Spy import Spy
from src.classes.characters.Warrior import Warrior
from src.crossover.Annular import Annular
from src.crossover.OnePoint import OnePoint
from src.crossover.TwoPoint import TwoPoint
from src.crossover.Uniform import Uniform
from src.cutoff.Content import Content
from src.cutoff.MaxGeneration import MaxGeneration
from src.cutoff.OptimumEnviroment import OptimumEnviroment
from src.cutoff.Structure import Structure
from src.mutation.CompleteMutation import CompleteMutation
from src.mutation.LimitedMultigeneMutation import LimitedMultigeneMutation
from src.mutation.SingleGeneMutation import SingleGeneMutation
from src.mutation.UniformMultiGeneMutation import UniformMultigeneMutation
from src.replacement.Traditional import Traditional
from src.replacement.YoungBias import YoungBias
from src.selection.SelectionFactory import SelectionFactory

CHARACTERS = {
    "warrior": Warrior,
    "archer": Archer,
    "defender": Defender,
    "spy": Spy}

CROSSOVER = {
    "one-point": OnePoint,
    "two-point": TwoPoint,
    "annular": Annular,
    "uniform": Uniform
}

MUTATION = {
    "single": SingleGeneMutation,
    "limited": LimitedMultigeneMutation,
    "uniform": UniformMultigeneMutation,
    "complete": CompleteMutation
}

REPLACEMENT = {
    "traditional": Traditional,
    "young": YoungBias
}
CUTOFF = {
    "content": Content,
    "max-generation": MaxGeneration,
    "optimum-environment": OptimumEnviroment,
    "structure": Structure
}


class Config:

    def __init__(self, config_file, seed=None):
        config_path = os.path.join(config_file)

        with open(config_path, "r") as f:
            config = json.load(f)
            self.character = CHARACTERS[config['character']]
            self.crossover = CROSSOVER[config['crossover']]
            self.mutation = MUTATION[config['mutation']['type']]
            self.mutation_probability = config['mutation']['probability']

            self.first_selection = SelectionFactory.configure(config['selection']['first-selection']['type'],
                                                              **config['selection']['first-selection']['parameters'])
            self.second_selection = SelectionFactory.configure(config['selection']['second-selection']['type'],
                                                               **config['selection']['second-selection']['parameters'])

            self.a_value = config['selection']['a-value']
            self.individuals = config['selection']['individuals']

            self.replacement_type = REPLACEMENT[config['replacement']['type']]
            self.replacement_first_selection = SelectionFactory.configure(
                config['replacement']['first-selection']['type'],
                **config['replacement']['first-selection']['parameters'])
            self.replacement_second_selection = SelectionFactory.configure(
                config['replacement']['second-selection']['type'],
                **config['replacement']['second-selection']['parameters'])

            self.b_value = config['replacement']['b-value']

            self.cutoff = CUTOFF[config['cutoff']['type']]
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
