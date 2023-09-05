import sys
import random

from Config import Config

# Argument constants
ARG_HELP = "help"
ARG_FILE = "file"

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


def execute_selection(population, individuals, first_selection, selection_probability, second_selection):
    #FIXME: missing second selection
    new_population = first_selection.select(population, individuals)
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

        genotypes = config.genotypes
        for i in range(config.cutoff_parameter):
            new_genotypes = execute_crossover(genotypes, config.crossover)
            mutated_genotypes = execute_mutation(new_genotypes, config.mutation, config.mutation_probability)
            population = get_population(mutated_genotypes, config.character)
            selection = execute_selection(population, config.individuals, config.first_selection,
                                          config.selection_probability, config.second_selection)
            print("-------------------------------------------------------------")
            print("Generation: " + i.__str__())
            for individual in selection:
                print(individual)
                print(individual.fitness())
            genotypes = get_genotypes(selection)


if __name__ == "__main__":
    main()
