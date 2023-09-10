import os
import pandas as pd
from src.benchmarks.dataframe.best_crossover_df import best_crossover_df
from src.benchmarks.dataframe.best_selection_df import best_selection_df
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
from src.benchmarks.plot.best_selection_plot import best_selection_plot

from src.utils.FileUtils import FileUtils

OUTPUT_DIR_PATH = os.path.join(os.path.dirname(__file__), 'output')
FileUtils.exists_or_create_dir(OUTPUT_DIR_PATH)


def get_output_path(filename: str):
    return os.path.join(OUTPUT_DIR_PATH, filename)

#df = best_crossover_df()
#df.to_csv(get_output_path("best_crossover"))
df = best_selection_df()
df.to_csv(get_output_path("best_selection"))
best_selection_plot(pd.read_csv('output/best_selection'))
#best_crossover_by_fitness_plot(df)
#best_crossover_by_generation_plot(df)
#best_crossover_avg_fitness_plot(df)
#best_crossover_avg_generation_plot(df)

# df = best_crossover_df()
# df.to_csv(get_output_path("best_crossover"))
# best_crossover_by_fitness_plot(df)
# best_crossover_by_generation_plot(df)
# best_crossover_avg_fitness_plot(df)
# best_crossover_avg_generation_plot(df)

# df = best_mutation_df()
# df.to_csv(get_output_path("best_mutation"))
# best_mutation_plot(df)

df = best_replacement_df()
df.to_csv(get_output_path("best_replacement"))
best_replacement_by_generations_plot(df)
best_replacement_by_fitness_plot(df)
best_replacement_avg_fitness_plot(df)
best_replacement_avg_generations_plot(df)
