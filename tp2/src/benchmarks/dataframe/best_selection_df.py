import json
import os
from Config import Config
from cli import get_population
from cli import get_genotypes
from cli import execute_crossover
from cli import execute_mutation
from cli import execute_selection
from cli import execute_replacement
from cli import cutoff
from pandas import DataFrame
from src.classes.characters.CharacterABC import CharacterABC
from src.selection.SelectionFactory import SelectionFactory
from src.utils.ConfigUtils import ConfigUtils

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir, "config.json")

with open(CONFIG_PATH, "r") as f:
    file = json.load(f)
    character = file["benchmarks"]["best_selection"]["character"]
    selection_methods = file["benchmarks"]["best_selection"]["selections"]
    iterations = file["benchmarks"]["best_selection"]["iterations"]

config = Config(CONFIG_PATH)


def get_selection_class(selection_name, file):
    if selection_name == 'deterministic':
        return SelectionFactory.configure(selection_name, **file["benchmarks"]["best_selection"][
            "deterministic-parameters"])
    elif selection_name == 'boltzmann':
        return SelectionFactory.configure(selection_name,
                                          **file["benchmarks"]["best_selection"][
                                              "boltzmann-parameters"])
    else:
        return SelectionFactory.configure(selection_name, **{})


def best_selection_df():
    rows = []

    for iteration in range(1, iterations + 1):
        generation = get_population(config.genotypes, ConfigUtils.CHARACTERS[character])
        for selection1 in selection_methods:
            selection1_class = get_selection_class(selection1, file)
            for selection2 in selection_methods:
                generation_count = 0

                old_populations = []
                i = 0

                selection2_class = get_selection_class(selection2, file)

                while cutoff(generation, old_populations, config.cutoff_parameter, i, config.cutoff) is False:
                    selection = execute_selection(generation, config.individuals, selection1_class,
                                                  selection2_class, config.a_value)
                    selection_genotypes = get_genotypes(selection)
                    crossover_genotypes = execute_crossover(selection_genotypes, config.crossover)
                    mutated_genotypes = execute_mutation(crossover_genotypes, config.mutation,
                                                         config.mutation_probability)
                    children = get_population(mutated_genotypes, ConfigUtils.CHARACTERS(character))
                    generation = execute_replacement(generation, children, config.replacement_type,
                                                     config.replacement_first_selection,
                                                     config.replacement_second_selection, config.b_value)
                    generation_count += 1
                    old_populations.append(generation)
                    i += 1

                best: CharacterABC = max(generation)
                rows.append({"iteration": iteration, "character": character, "selection1": selection1,
                             "selection2": selection2, "fitness": best.fitness(), "generation": generation_count})

    return DataFrame(rows)
