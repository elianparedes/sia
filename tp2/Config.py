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
from src.mutation import UniformMultiGeneMutation
from src.mutation.CompleteMutation import CompleteMutation
from src.mutation.LimitedMultigeneMutation import LimitedMultigeneMutation
from src.mutation.SingleGeneMutation import SingleGeneMutation
from src.selection.Boltzmann import Boltzmann
from src.selection.DeterministicTournament import DeterministicTournament
from src.selection.Elite import Elite
from src.selection.ProbabilisticTournament import ProbabilisticTournament
from src.selection.Ranked import Ranked
from src.selection.Roulette import Roulette
from src.selection.SelectionFactory import SelectionFactory
from src.selection.Universal import Universal

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
    "uniform": UniformMultiGeneMutation,
    "complete": CompleteMutation
}

SELECTION = {
    "elite": Elite,
    "roulette": Roulette,
    "universal": Universal,
    "ranked": Ranked,
    "boltzmann": Boltzmann,
    "deterministic": DeterministicTournament,
    "probabilistic": ProbabilisticTournament
}


class Config:

    def __init__(self, config_file):
        config_path = os.path.join(config_file)

        with open(config_path, "r") as f:
            config = json.load(f)
            self.character = CHARACTERS[config['character']]
            self.crossover = CROSSOVER[config['crossover']]
            self.mutation = MUTATION[config['mutation']['type']]
            self.mutation_probability = config['mutation']['probability']

            first_selection = config['selection']['first']['type']
            if first_selection == 'boltzmann':
                self.first_selection = SelectionFactory.configure(first_selection,
                                                                  **config['selection']['boltzmann-parameters'])
            elif first_selection == 'deterministic':
                self.first_selection = SelectionFactory.configure(first_selection,
                                                                  **config['selection']['deterministic-parameters'])
            else:
                self.first_selection = SelectionFactory.configure(first_selection, **{})
            self.selection_probability = config['selection']['first']['probability']

            second_selection = config['selection']['second']['type']
            if second_selection == 'boltzmann':
                self.second_selection = SelectionFactory.configure(second_selection,
                                                                  **config['selection']['boltzmann-parameters'])
            elif second_selection == 'deterministic':
                self.second_selection = SelectionFactory.configure(second_selection,
                                                                  **config['selection']['deterministic-parameters'])
            else:
                self.second_selection = SelectionFactory.configure(second_selection, **{})
            self.individuals = config['selection']['individuals']

            self.replacement = config['replacement']
            self.cutoff = config['cutoff']['type']
            self.cutoff_parameter = config['cutoff']['parameter']
            self.genotypes = []
            for genotype in config['seed']:
                self.genotypes.append(
                    Genotype(genotype["strength"], genotype["agility"], genotype["skill"], genotype["endurance"],
                             genotype["health"],
                             genotype["height"]))
