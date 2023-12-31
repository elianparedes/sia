from src.classes.Config import Config
from src.benchmarks.df.algorithms import algorithms_benchmark_df
from src.benchmarks.plot.algorithms import algorithms_benchmarks_plot
from src.benchmarks.df.heatmaps import algorithms_heatmap_df
from src.benchmarks.plot.heatmaps import algorithms_heatmaps_plot
from src.benchmarks.df.heuristic import heuristics_benchmark_df
from src.benchmarks.plot.heuristic import heuristics_benchmarks_plot
from src.benchmarks.plot.heuristic_time import heuristics_time_benchmarks_plot
from src.benchmarks.df.nodes_expanded import nodes_expanded_benchmarks_df
from src.benchmarks.plot.nodes_expanded import nodes_expanded_benchmarks_plot
import os
import pandas as pd

OUTPUT_PATH=os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "output")

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

config = Config()
benchmarks = {
    'algorithms': {
        'df': algorithms_benchmark_df,
        'plot': [algorithms_benchmarks_plot]
    },
    'heatmap': {
        'df': algorithms_heatmap_df,
        'plot': [algorithms_heatmaps_plot]
    },
    'heuristic': {
        'df': heuristics_benchmark_df,
        'plot': [heuristics_benchmarks_plot, heuristics_time_benchmarks_plot]
    },
    'nodes_expanded': {
        'df': nodes_expanded_benchmarks_df,
        'plot': [nodes_expanded_benchmarks_plot]
    }
}

for benchmark_name in config.benchmarks.keys():
    print(f"Running {benchmark_name}.py")
    benchmark_functions = benchmarks[benchmark_name]

    if config.dataframe:
        df = benchmark_functions['df'](config.benchmarks[benchmark_name])
        if config.export_csv:
            df.to_csv(os.path.join(OUTPUT_PATH, benchmark_name + '_df.csv'), index=False)

    if config.plot:
        if not config.dataframe:
            df = pd.read_csv(os.path.join(OUTPUT_PATH, benchmark_name + '_df.csv'))
        for function in benchmark_functions['plot']:
            function(df)
    print("---------------------------------------------------------------")
