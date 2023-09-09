import os

from src.benchmarks.dataframe.best_crossover_df import best_crossover_df
from src.benchmarks.plot.best_crossover_plot import best_crossover_plot

from src.benchmarks.dataframe.best_mutation_df import best_mutation_df
from src.benchmarks.plot.best_mutation_plot import best_mutation_plot

from src.utils.FileUtils import FileUtils

OUTPUT_DIR_PATH = os.path.join(os.path.dirname(__file__), 'output')
FileUtils.exists_or_create_dir(OUTPUT_DIR_PATH)

def get_output_path(filename: str):
    return os.path.join(OUTPUT_DIR_PATH, filename)

# df = best_crossover_df()
# df.to_csv(get_output_path("best_crossover"))
# best_crossover_plot(df)

df = best_mutation_df()
df.to_csv(get_output_path("best_mutation"))
best_mutation_plot(df)