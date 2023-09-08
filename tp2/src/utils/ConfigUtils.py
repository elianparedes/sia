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


class ConfigUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

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

