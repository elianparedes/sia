from src.benchmarks.dataframe.best_crossover_df import best_crossover_df
from src.benchmarks.plot.best_crossover_plot import best_crossover_plot

df = best_crossover_df()
df.to_csv("best_crossover")
best_crossover_plot()