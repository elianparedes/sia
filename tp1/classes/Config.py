import os
import json

from algorithms.AStar import AStar
from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.LocalGreedy import LocalGreedy
from algorithms.GlobalGreedy import GlobalGreedy

from classes.FileUtils import FileUtils


class Config:
    def __init__(self, config_key):
        all_algorithms = {
            "bfs": BFS.execute,
            "dfs": DFS.execute,
            "a-star": AStar.execute,
            "local_greedy": LocalGreedy.execute,
            "global_greedy": GlobalGreedy.execute
        }

        config_path = os.path.join(os.path.dirname(__file__), os.pardir, "config.json")

        with open(config_path, "r") as f:
            config = json.load(f)
            config = config[config_key]
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