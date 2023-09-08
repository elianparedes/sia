import sys
import random
from math import ceil, floor
from typing import List

from Config import Config
from src.classes.Genotype import Genotype

# Argument constants
ARG_HELP = "help"
ARG_FILE = "file"
ARG_SEED = "seed"

CUTOFF = {}

DEFAULT_CONFIG_FILE = 'config.json'

MIN_POINTS = 0
MAX_POINTS = 100
MIN_HEIGHT = 1.3
MAX_HEIGHT = 2.0
GENOTYPE = {"strength", "agility", "skill", "endurance", "health", "height"}


def show_help():
    print("Usage: python cli.py [-f <file_name>] [-s <qty>] [-h]")
    print(f"-f, --{ARG_FILE}    <file_name>")
    print("\tThe name of the config file. It defaults to `config.json`.")
    print(f"-s, --{ARG_SEED}    <qty>")
    print("\tGenerates a random seed with <qty> individuals.")
    print(f"-h, --{ARG_HELP}")
    print("\tPrint usage.")
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


def execute_selection(population, individuals, first_selection, second_selection, a_value):
    return first_selection.select(population, ceil(individuals * a_value)) \
        + second_selection.select(population, floor(individuals * (1 - a_value)))


def execute_replacement(population, children, replacement, first_selection, second_selection, b_value):
    return replacement.replace(population, children, first_selection, second_selection, b_value)


def cutoff(population, oldPopulations, cutoff_parameter, generation, cutoff_type):
    return cutoff_type.cutoff(population, oldPopulations, generation, cutoff_parameter)


def randomize_seed(qty: int) -> List[Genotype]:
    seed = []
    genotype = {}
    for _ in range(qty):
        for gene in GENOTYPE:
            genotype[gene] = random.uniform(MIN_POINTS, MAX_POINTS) if gene != "height" else random.uniform(MIN_HEIGHT,
                                                                                                            MAX_HEIGHT)

        seed.append(Genotype(genotype["strength"], genotype["agility"], genotype["skill"], genotype["endurance"],
                             genotype["health"], genotype["height"]))

    return seed


def main():
    args = {ARG_HELP: False, ARG_FILE: None, ARG_SEED: 0}

    # Parse command-line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg in ("-f", f"--{ARG_FILE}"):
            i += 1
            args[ARG_FILE] = sys.argv[i] if i < len(sys.argv) else None
        if arg in ("-s", f"--{ARG_SEED}"):
            i += 1
            args[ARG_SEED] = sys.argv[i] if i < len(sys.argv) else None
        elif arg in ("-h", f"--{ARG_HELP}"):
            args[ARG_HELP] = True

        i += 1

    # Your main script logic here
    config_file = args[ARG_FILE] if args[ARG_FILE] is not None else DEFAULT_CONFIG_FILE
    help_flag = args[ARG_HELP]
    individual_qty = int(args[ARG_SEED])

    if help_flag:
        show_help()
        exit(0)
    else:

        if individual_qty == 0:
            config = Config(config_file)
        else:
            config = Config(config_file, randomize_seed(individual_qty))

        generation = get_population(config.genotypes, config.character)
        oldPopulations = []
        i = 0
        while cutoff(generation, oldPopulations, config.cutoff_parameter, i, config.cutoff) is False:
            selection = execute_selection(generation, config.individuals, config.first_selection,
                                          config.second_selection, config.a_value)
            selection_genotypes = get_genotypes(selection)
            crossover_genotypes = execute_crossover(selection_genotypes, config.crossover)
            mutated_genotypes = execute_mutation(crossover_genotypes, config.mutation, config.mutation_probability)
            children = get_population(mutated_genotypes, config.character)
            generation = execute_replacement(generation, children, config.replacement_type,
                                             config.replacement_first_selection,
                                             config.replacement_second_selection, config.b_value)
            oldPopulations.append(generation)
            i += 1
            print("-------------------------------------------------------------")
            print("Generation: " + i.__str__())
            for individual in generation:
                print(individual)
                print("fitness: " + individual.fitness().__str__())


if __name__ == "__main__":
    main()
