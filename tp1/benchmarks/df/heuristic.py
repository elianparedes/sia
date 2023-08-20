import pandas as pd

from classes.Config import Config
from classes.SokobanUtils import SokobanUtils
from classes.State import State
from classes.StateUtils import StateUtils

from heuristics.ManhattanDistance import ManhattanDistance
from heuristics.MinDistance import MinDistance
from heuristics.HeuristicCombination import HeuristicCombination
from heuristics.BipartiteHeuristic import BipartiteHeuristic

def heuristics_benchmark_df():
    config = Config("heuristic")

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

        deadlocks = StateUtils.obtain_deadlocks(walls, blanks)

        state_wdeadlocks = State(set(boxes), set(
            walls), player, set(goals), set(deadlocks))

        print(f"Solving {map_name} map")

        for algorithm, alg_function in config.algorithms.items():
            for heuristic in heuristics:
                print(f"Executing {algorithm} with deadlocks and with heuristic {heuristic['name']}")

                nodes, expanded_nodes, frontier = alg_function(state_wdeadlocks, heuristic["function"])

                data_rows.append(
                    {"map": map_name, "algorithm": algorithm, "expanded_nodes": expanded_nodes, "heuristic": heuristic['name']})

    return pd.DataFrame(data_rows)