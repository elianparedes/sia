import json
import os
from math import ceil, floor

from Config import Config
from cli import get_population
from cli import get_genotypes
from cli import execute_crossover
from cli import execute_mutation
from cli import execute_selection
from cli import execute_replacement
from cli import cutoff
from cli import randomize_seed
from pandas import DataFrame
from src.classes.characters.CharacterABC import CharacterABC
from src.utils.ConfigUtils import ConfigUtils

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir, "config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)
    characters = config["benchmarks"]["seed_quantity"]["characters"]
    iterations = config["benchmarks"]["seed_quantity"]["iterations"]
    initial = config["benchmarks"]["seed_quantity"]["initial"]
    step = config["benchmarks"]["seed_quantity"]["step"]

config = Config(CONFIG_PATH)


def seed_quantity_df():

    rows = []
    randomized_seeds = {}
    for i in range(initial, initial + step * 5 + 1, step):
        randomized_seeds[i] = randomize_seed(i)

    for character in characters:
        for quantity in range(initial, initial + step * 5 + 1, step):
            individuals = floor(quantity*0.75)
            for iteration in range(1, iterations + 1):
                generation = get_population(randomized_seeds[quantity], ConfigUtils.CHARACTERS[character])
                old_populations = []
                generation_count = 0

                while cutoff(generation, old_populations, config.cutoff_parameter, generation_count, config.cutoff) is False:
                    selection = execute_selection(generation, individuals, config.first_selection,
                                                  config.second_selection, config.a_value)
                    selection_genotypes = get_genotypes(selection)
                    crossover_genotypes = execute_crossover(selection_genotypes, config.crossover)
                    mutated_genotypes = execute_mutation(crossover_genotypes, config.mutation,
                                                         config.mutation_probability)
                    children = get_population(mutated_genotypes, ConfigUtils.CHARACTERS[character])
                    generation = execute_replacement(generation, children, config.replacement_type,
                                                     config.replacement_first_selection,
                                                     config.replacement_second_selection, config.b_value)

                    old_populations.append(generation)
                    generation_count += 1

                best: CharacterABC = max(generation)
                rows.append({"iteration": iteration, "character": character, "quantity": quantity,
                             "fitness": best.fitness(), "generation": generation_count, "genes": str(best.gene)})

    return DataFrame(rows)
