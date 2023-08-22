import os
import time
import pandas as pd

from classes.SokobanUtils import SokobanUtils
from classes.State import State
from classes.StateUtils import StateUtils

CSV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "output", "algorithms_df.csv")


def algorithms_benchmark_df(config):

    data_rows = []

    for map_name,map in config.maps.items():
        parsed_contents = SokobanUtils.parse_sokoban_board(map)

        walls = parsed_contents.get('wall', [])
        blanks = parsed_contents.get('blank', [])
        boxes = parsed_contents.get('box', [])
        player = parsed_contents.get('player', [])[0]
        goals = parsed_contents.get('goal', [])

        deadlocks = StateUtils.obtain_deadlocks(walls, goals)

        state = State(set(boxes), set(walls), player, set(goals), set([]))
        state_wdeadlocks = State(set(boxes), set(
            walls), player, set(goals), set(deadlocks))

        print(f"Solving {map_name} map")

        for algorithm, alg_function in config.algorithms.items():
            for _ in range(10):
                print(f"Executing {algorithm} without deadlocks")

                start_time = time.time()
                alg_function(state)
                end_time = time.time() - start_time

                print(f"Executing {algorithm} with deadlocks")

                start_time = time.time()
                alg_function(state_wdeadlocks)
                end_time_wdeadlocks = time.time() - start_time

                data_rows.append(
                    {"map": map_name, "algorithm": algorithm, "without_deadlocks": end_time, "with_deadlocks": end_time_wdeadlocks})

    df = pd.DataFrame(data_rows)
    df.to_csv(CSV_PATH)
