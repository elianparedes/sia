import time
import pandas as pd

from src.classes.Config import Config
from src.classes.SokobanUtils import SokobanUtils
from src.classes.State import State
from src.classes.StateUtils import StateUtils

def nodes_expanded_benchmarks_df(config):
    data_rows = []

    for map_name,map in config.maps.items():
        parsed_contents = SokobanUtils.parse_sokoban_board(map)

        walls = parsed_contents.get('wall', [])
        boxes = parsed_contents.get('box', [])
        player = parsed_contents.get('player', [])[0]
        goals = parsed_contents.get('goal', [])

        deadlocks = StateUtils.obtain_deadlocks(walls, goals)

        state = State(set(boxes), set(walls), player, set(goals), set([]))
        state_wdeadlocks = State(set(boxes), set(
            walls), player, set(goals), set(deadlocks))

        print(f"Solving {map_name} map")

        for algorithm, alg_function in config.algorithms.items():
            print(f"Executing {algorithm} without deadlocks")

            solution = alg_function(state)

            print(f"Executing {algorithm} with deadlocks")

            solution_wdeadlocks = alg_function(state_wdeadlocks)

            data_rows.append(
                {"map": map_name, "algorithm": algorithm, "without_deadlocks": solution[1], "with_deadlocks": solution_wdeadlocks[1]})

    return pd.DataFrame(data_rows)