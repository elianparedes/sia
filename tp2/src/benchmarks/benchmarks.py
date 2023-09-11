import os
import json
import pandas as pd
from src.benchmarks.dataframe.best_crossover_df import best_crossover_df
from src.benchmarks.dataframe.best_selection_df import best_selection_df
from src.benchmarks.dataframe.global_analisis import global_analisis_df
from src.benchmarks.plot.best_crossover_plot import best_crossover_by_fitness_plot, best_crossover_for_character
from src.benchmarks.plot.best_crossover_plot import best_crossover_by_generation_plot
from src.benchmarks.plot.best_crossover_plot import best_crossover_avg_fitness_plot
from src.benchmarks.plot.best_crossover_plot import best_crossover_avg_generation_plot
from src.benchmarks.dataframe.best_mutation_df import best_mutation_df
from src.benchmarks.plot.best_mutation_plot import best_mutation_plot
from src.benchmarks.dataframe.best_replacement import best_replacement_df
from src.benchmarks.plot.best_replacement import best_replacement_by_generations_plot
from src.benchmarks.plot.best_replacement import best_replacement_by_fitness_plot
from src.benchmarks.plot.best_replacement import best_replacement_avg_fitness_plot
from src.benchmarks.plot.best_replacement import best_replacement_avg_generations_plot
from src.benchmarks.plot.best_selection_plot import best_selection_by_fitness_plot, best_selection_by_generation_plot
from src.benchmarks.plot.global_analysis_plot import global_analysis_avg

from src.utils.FileUtils import FileUtils

OUTPUT_DIR_PATH = os.path.join(os.path.dirname(__file__), 'output')
FileUtils.exists_or_create_dir(OUTPUT_DIR_PATH)

benchmarks = \
    {
        "best_crossover":
            {
                "df": best_crossover_df,
                "plot_functions": [best_crossover_by_generation_plot, best_crossover_by_fitness_plot,
                                   best_crossover_avg_generation_plot, best_crossover_avg_fitness_plot],
            },
        "best_mutation":
            {
                "df": best_mutation_df,
                "plot_functions": [best_mutation_plot],
            },
        "best_replacement":
            {
                "df": best_replacement_df,
                "plot_functions": [best_replacement_by_generations_plot, best_replacement_by_fitness_plot,
                                   best_replacement_avg_fitness_plot, best_replacement_avg_generations_plot],
            },
        "best_selection":
            {
                "df": best_selection_df,
                "plot_functions": [best_selection_by_fitness_plot, best_selection_by_generation_plot],
            },
        "best_global_analisis":
            {
                "df": global_analisis_df,
                "plot_functions": [global_analysis_avg],
            }
    }

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, "config.json")

with open(CONFIG_PATH, "r") as f:
    file = json.load(f)
    run = file["benchmarks"]["run"]

    for benchmark in run:
        benchmarks[benchmark]["plot"] = file["benchmarks"][benchmark]["plot"]
        benchmarks[benchmark]["export_csv"] = file["benchmarks"][benchmark]["export_csv"]


def get_output_path(filename: str):
    return os.path.join(OUTPUT_DIR_PATH, filename)


for benchmark in run:
    df = None
    if benchmarks[benchmark]["export_csv"]:
        df = benchmarks[benchmark]["df"]()
        df.to_csv(get_output_path(benchmark))
    if benchmarks[benchmark]["plot"]:
        if benchmarks[benchmark]["export_csv"] is False:
            df = pd.read_csv(get_output_path(benchmark))
        for function in benchmarks[benchmark]["plot_functions"]:
            function(df)
