import os
import json

from src.algorithms.AStar import AStar
from src.algorithms.BFS import BFS
from src.algorithms.DFS import DFS
from src.algorithms.LocalGreedy import LocalGreedy
from src.algorithms.GlobalGreedy import GlobalGreedy

from src.classes.FileUtils import FileUtils


class Config:
    class BenchmarkConfig:
        def __init__(self, config):
            all_algorithms = {
                "bfs": BFS.execute,
                "dfs": DFS.execute,
                "a-star": AStar.execute,
                "local_greedy": LocalGreedy.execute,
                "global_greedy": GlobalGreedy.execute
            }

            deadlocks = config["deadlocks"]
            maps_names = config.get("maps", [])
            algorithms_names = config.get("algorithms", [])

            self.deadlocks = deadlocks

            if algorithms_names:
                self.algorithms = {name: all_algorithms[name] for name in algorithms_names if name in all_algorithms}
            else:
                self.algorithms = all_algorithms

            maps_dir = os.path.join(os.path.dirname(
                __file__), os.pardir,
                "resources", "maps")

            if not maps_names:
                maps_names = [os.path.splitext(filename)[0] for filename in os.listdir(maps_dir) if
                              filename.endswith('.txt')]
                maps_names.sort()

            self.maps = {}
            for map_name in maps_names:
                map_path = os.path.join(maps_dir, map_name + ".txt")
                self.maps[map_name] = FileUtils.open_map(map_path)

    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), os.pardir, "config.json")

        with open(config_path, "r") as f:
            config = json.load(f)
            settings = config['settings']
            benchmark = config['benchmarks']
        self.export_csv = benchmark['export_csv']
        self.plot = benchmark['plot']
        self.dataframe = benchmark['dataframe']
        self.benchmarks = {}
        for benchmark in benchmark['run']:
            benchmark_config = self.BenchmarkConfig(settings[benchmark])
            self.benchmarks[benchmark] = benchmark_config
