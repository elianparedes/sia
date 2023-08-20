from df.heatmaps import algorithms_heatmap_df
from plot.heatmaps import algorithms_heatmaps_plot
from df.algorithms import algorithms_benchmark_df
from plot.algorithms import algorithms_benchmarks_plot

#df = algorithms_heatmap_df()
#algorithms_heatmaps_plot(df)

df = algorithms_benchmark_df()
algorithms_benchmarks_plot(df)
