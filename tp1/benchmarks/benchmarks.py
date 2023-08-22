from classes.Config import Config
from benchmarks.df.algorithms import algorithms_benchmark_df
from benchmarks.plot.algorithms import algorithms_benchmarks_plot
from benchmarks.df.heatmaps import algorithms_heatmap_df
from benchmarks.plot.heatmaps import algorithms_heatmaps_plot
from benchmarks.df.heuristic import heuristics_benchmark_df
from benchmarks.plot.heuristic import heuristics_benchmarks_plot
from benchmarks.plot.heuristic_time import heuristics_time_benchmarks_plot
import os
import pandas as pd

if not os.path.exists('../output'):
    os.makedirs('../output')

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
    }
}

for benchmark_name in config.benchmarks.keys():
    print(f"Running {benchmark_name}.py")
    benchmark_functions = benchmarks[benchmark_name]

    if config.dataframe:
        df = benchmark_functions['df'](config.benchmarks[benchmark_name])
        if config.export_csv:
            df.to_csv('../output/' + benchmark_name + '_df.csv', index=False)

    if config.plot:
        if not config.dataframe:
            df = pd.read_csv('../output/' + benchmark_name + '_df.csv')
        for function in benchmark_functions['plot']:
            function(df)
    print("---------------------------------------------------------------")
