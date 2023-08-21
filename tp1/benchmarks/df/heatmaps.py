import pandas as pd
import numpy as np

from classes.SokobanUtils import SokobanUtils
from classes.StateUtils import StateUtils
from classes.State import State
from classes.Config import Config

def get_player_heatmap(map_solution, map_width, map_height):
    max_side = max(map_width, map_height)
    map_points = np.array([np.array([0 for _ in range(max_side)]) for _ in range(max_side)])

    node = map_solution[0]
    depth = map_solution[1]
    stack = []

    while node is not None:
        stack.append((node, depth))
        node = node.father
        depth += 1

    while stack:
        node, depth = stack.pop()
        player_point = node.state.player_point
        map_points[player_point.x][player_point.y] += 1

    return map_points

def get_map_bounding_box(map_contents: str):
    lines = map_contents.strip().split('\n')

    widest_line = max(lines, key=len)

    width = len(widest_line)
    height = len(lines)

    return width, height


def open_map(map_path):
    try:
        with open(map_path, "r") as map_file:
            map_contents = map_file.read()
    except FileNotFoundError:
        print(f"Map '{map_path}' not found.")
        print("Make sure it is under the resources/maps folder.")
        exit(1)

    return map_contents


def algorithms_heatmap_df(config):

    if len(config.maps.values()) > 1:
        raise RuntimeError("Method supports only one map")

    for map in config.maps.values():
        width, height = get_map_bounding_box(map)
        parsed_contents = SokobanUtils.parse_sokoban_board(map)

        walls = parsed_contents.get('wall', [])
        blanks = parsed_contents.get('blank', [])
        boxes = parsed_contents.get('box', [])
        player = parsed_contents.get('player', [])[0]
        goals = parsed_contents.get('goal', [])

        deadlocks = StateUtils.obtain_deadlocks(walls,goals)

        state = State(set(boxes), set(walls), player, set(goals), set([]))
        state_wdeadlocks = State(set(boxes), set(walls), player, set(goals), set(deadlocks))

        heatmaps = []
        for algorithm, alg_function in config.algorithms.items():
            solution = alg_function(state)
            player_heatmap = get_player_heatmap(solution, width, height)

            solution_wdeadlocks = alg_function(state_wdeadlocks)
            player_heatmap_wdeadlocks = get_player_heatmap(solution_wdeadlocks, width, height)

            heatmaps.append({"algorithm": algorithm, "without_deadlocks": player_heatmap, "with_deadlocks": player_heatmap_wdeadlocks})

        return pd.DataFrame(heatmaps)
