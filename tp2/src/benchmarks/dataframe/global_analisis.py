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
    character = file["benchmarks"]["best_global_analisis"]["character"]
    iterations = file["benchmarks"]["best_selection"]["iterations"]

config = Config(CONFIG_PATH)


def global_analisis_df():
    rows = []
    for char in ConfigUtils.CHARACTERS.keys():
        generation = get_population(config.genotypes,  ConfigUtils.CHARACTERS[char])
        selection1_class = config.first_selection
        generation_count = 0
        old_populations = []
        i = 0
        selection2_class = config.second_selection
        while cutoff(generation, old_populations, config.cutoff_parameter, i, config.cutoff) is False:
            selection = execute_selection(generation, config.individuals, selection1_class,
                                          selection2_class, config.a_value)
            selection_genotypes = get_genotypes(selection)
            crossover_genotypes = execute_crossover(selection_genotypes, config.crossover)
            mutated_genotypes = execute_mutation(crossover_genotypes, config.mutation,
                                                 config.mutation_probability)
            children = get_population(mutated_genotypes,  ConfigUtils.CHARACTERS[char])
            generation = execute_replacement(generation, children, config.replacement_type,
                                             config.replacement_first_selection,
                                             config.replacement_second_selection, config.b_value)
            generation_count += 1
            old_populations.append(generation)
            i += 1
            best: CharacterABC = max(generation)
            rows.append({"iteration": i, "type": "health", "value": best.get_gene().health.value, "character": char})
            rows.append({"iteration": i, "type": "intelligence",
                         "value": best.get_gene().intelligence.value,"character": char})
            rows.append(
                {"iteration": i, "type": "strength", "value": best.get_gene().strength.value,"character": char})
            rows.append({"iteration": i, "type": "agility", "value": best.get_gene().agility.value,"character": char})
            rows.append({"iteration": i, "type": "endurance", "value": best.get_gene().endurance.value,"character": char})
    return DataFrame(rows)
