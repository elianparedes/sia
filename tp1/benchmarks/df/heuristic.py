import os
import time
import pandas as pd

from classes.Config import Config
from classes.SokobanUtils import SokobanUtils
from classes.State import State
from classes.StateUtils import StateUtils

from heuristics.ManhattanDistance import ManhattanDistance
from heuristics.MinDistance import MinDistance
from heuristics.HeuristicCombination import HeuristicCombination
from heuristics.BipartiteHeuristic import BipartiteHeuristic

CSV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "output", "heuristic.csv")

def heuristics_benchmark_df(config):

    data_rows = []

    heuristics = [
        {"name": "manhattan_distance", "function": ManhattanDistance},
        {"name": "min_distance", "function": MinDistance},
        {"name": "heuristic_combination", "function": HeuristicCombination},
        {"name": "bipartite", "function": BipartiteHeuristic}
    ]

    for map_name,map in config.maps.items():
        parsed_contents = SokobanUtils.parse_sokoban_board(map)

        walls = parsed_contents.get('wall', [])
        blanks = parsed_contents.get('blank', [])
        boxes = parsed_contents.get('box', [])
        player = parsed_contents.get('player', [])[0]
        goals = parsed_contents.get('goal', [])

        deadlocks = StateUtils.obtain_deadlocks(walls, goals)

        state_wdeadlocks = State(set(boxes), set(
            walls), player, set(goals), set(deadlocks))

        print(f"Solving {map_name} map")

        for algorithm, alg_function in config.algorithms.items():
            for heuristic in heuristics:
                for _ in range(10):
                    print(f"Executing {algorithm} with deadlocks and with heuristic {heuristic['name']}")

                    start_time = time.time()
                    nodes, expanded_nodes, frontier = alg_function(state_wdeadlocks, heuristic["function"])
                    end_time = time.time() - start_time

                    data_rows.append(
                        {"map": map_name, "algorithm": algorithm, "time": end_time,
                         "expanded_nodes": expanded_nodes, "heuristic": heuristic['name']})

    df = pd.DataFrame(data_rows)
    return df