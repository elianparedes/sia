import json
import os
import time
import pandas as pd

from algorithms.AStar import AStar
from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.LocalGreedy import LocalGreedy
from algorithms.GlobalGreedy import GlobalGreedy

from classes.SokobanUtils import SokobanUtils
from classes.State import State


def open_map(map_path):
    try:
        with open(map_path, "r") as map_file:
            map_contents = map_file.read()
    except FileNotFoundError:
        print(f"Map '{map_path}' not found.")
        print("Make sure it is under the resources/maps folder.")
        exit(1)

    return map_contents


def algorithms_benchmark_df():
    algorithms = [
        {"name": "bfs", "function": BFS.execute},
        {"name": "dfs", "function": DFS.execute},
        {"name": "a-star", "function": AStar.execute},
        {"name": "local_greedy", "function": LocalGreedy.execute},
        {"name": "global_greedy", "function": GlobalGreedy.execute},
    ]

    maps_dir = os.path.join(os.path.dirname(
        __file__), os.pardir, os.pardir,
        "resources", "maps")

    maps = os.listdir(maps_dir)
    maps.sort()

    data_rows = []

    for map in maps:
        map_path = os.path.join(maps_dir, map)
        map_name = os.path.splitext(os.path.basename(map))[0]

        map_contents = open_map(map_path)
        parsed_contents = SokobanUtils.parse_sokoban_board(map_contents)

        walls = parsed_contents.get('wall', [])
        blanks = parsed_contents.get('blank', [])
        boxes = parsed_contents.get('box', [])
        player = parsed_contents.get('player', [])[0]
        goals = parsed_contents.get('goal', [])

        deadlocks = SokobanUtils.get_deadlocks(walls, blanks)

        state = State(set(boxes), set(walls), player, set(goals), set([]))
        state_wdeadlocks = State(set(boxes), set(
            walls), player, set(goals), set(deadlocks))

        print(f"Solving {map} map")

        for algorithm in algorithms:
            print(f"Executing {algorithm['name']} without deadlocks")

            start_time = time.time()
            algorithm['function'](state)
            end_time = time.time() - start_time

            print(f"Executing {algorithm['name']} with deadlocks")

            start_time = time.time()
            algorithm['function'](state_wdeadlocks)
            end_time_wdeadlocks = time.time() - start_time

            data_rows.append(
                {"map": map_name, "algorithm": algorithm['name'], "without_deadlocks": end_time, "with_deadlocks": end_time_wdeadlocks})

    return pd.DataFrame(data_rows)