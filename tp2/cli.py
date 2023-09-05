import sys

from Config import Config
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
from src.selection.Universal import Universal

# Argument constants
ARG_HELP = "help"
ARG_FILE = "file"

CHARACTERS = {"warrior": Warrior,
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

SELECTION = {"elite": Elite,
             "roulette": Roulette,
             "universal": Universal,
             "ranked": Ranked,
             "boltzmann": Boltzmann,
             "deterministic": DeterministicTournament,
             "probabilistic": ProbabilisticTournament
             }

CUTOFF = {}


def show_help():
    print("Usage: python cli.py -f <file_name> [-h]")
    print(f"-h, --{ARG_FILE}")
    print("\tThe name of the config file")
    print(f"-h, --{ARG_HELP}")
    print("\tPrint usage")
    return


def get_population(genotypes, character_type):
    population = []

    for genotype in genotypes:
        population.append(character_type(genotype))
    return population


def get_genotypes(population):
    genotypes = []
    for individual in population:
        genotypes.append(individual.get_gene())

    return genotypes


def execute_crossover(genotypes, crossover_type):
    children_genotypes = []
    for i in range(0, len(genotypes), 2):
        if i + 1 < len(genotypes):
            child_tuple = crossover_type.cross(genotypes[i], genotypes[i + 1])
            children_genotypes.append(child_tuple[0])
            children_genotypes.append(child_tuple[1])
        else:
            children_genotypes.append(genotypes[i])

    return children_genotypes


def execute_mutation(genotypes, mutation_type, probability):
    mutated_genotypes = []
    for genotype in genotypes:
        mutated_genotypes.append(mutation_type.mutate(genotype, probability))
    return mutated_genotypes


def execute_selection(population, individuals, selection_type):
    new_population = selection_type.select(population, individuals)
    return new_population


def main():
    args = {ARG_HELP: False, ARG_FILE: None}

    # Parse command-line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg in ("-f", f"--{ARG_FILE}"):
            i += 1
            args[ARG_FILE] = sys.argv[i] if i < len(sys.argv) else None
        elif arg in ("-h", f"--{ARG_HELP}"):
            args[ARG_HELP] = True

        i += 1

    # Your main script logic here
    config_file = args[ARG_FILE]
    help_flag = args[ARG_HELP]

    if len(sys.argv) == 1 or help_flag:
        show_help()
        exit(0)
    else:
        if args[ARG_FILE] is None:
            print("Incorrect usage.")
            print("Type 'python cli.py -h' to get more help.")
            exit(1)

        config = Config(config_file)
        character_type = CHARACTERS[config.character]
        crossover_type = CROSSOVER[config.crossover]
        mutation_type = MUTATION[config.mutation]
        selection_type = SELECTION[config.selection]
        # cutoff_type = CUTOFF[config.cutoff] not implemented

        genotypes = config.genotypes
        for i in range(100):
            new_genotypes = execute_crossover(genotypes, crossover_type)
            mutated_genotypes = execute_mutation(new_genotypes, mutation_type, 0.5)
            population = get_population(mutated_genotypes, character_type)
            selection = execute_selection(population, 8, selection_type)
            print("-------------------------------------------------------------")
            print("Generation: " + i.__str__())
            for individual in selection:
                print(individual)
                print(individual.fitness())
            genotypes = get_genotypes(selection)


if __name__ == "__main__":
    main()
