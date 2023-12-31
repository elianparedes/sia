import pandas as pd
import numpy as np

from src.classes.SokobanUtils import SokobanUtils
from src.classes.StateUtils import StateUtils
from src.classes.State import State
from src.classes.Config import Config

from src.heuristics.BipartiteHeuristic import BipartiteHeuristic
from src.heuristics.ManhattanDistance import ManhattanDistance
from src.heuristics.MinDistance import MinDistance
from src.heuristics.HeuristicCombination import HeuristicCombination


def get_map_matrix(map_width, map_height):
    max_side = max(map_width, map_height)
    return np.array([np.array([0 for _ in range(max_side)]) for _ in range(max_side)])

def get_player_heatmap(map_solution, map_width, map_height):
    map_matrix = get_map_matrix(map_width, map_width)
    
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
        map_matrix[player_point.x][player_point.y] += 1

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

def append_player_position(state, map_matrix):
    player_point = state.player_point

    map_matrix[player_point.x][player_point.y] += 1

def append_boxes_position(state, map_matrix):
    boxes_points = state.boxes_points

    for box_points in boxes_points:
        map_matrix[box_points.x][box_points.y] += 1

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

            # !! use append_player_position instead for calculating player heatmap

            heatmap = get_map_matrix(width, height)
            alg_function(state, heuristic_fn=ManhattanDistance, on_state_change=lambda state: append_boxes_position(state, heatmap))

            heatmap_wdeadlocks = get_map_matrix(width, height)
            alg_function(state_wdeadlocks, heuristic_fn=ManhattanDistance, on_state_change=lambda state: append_boxes_position(state, heatmap_wdeadlocks))

            heatmaps.append({"algorithm": algorithm, "without_deadlocks": heatmap, "with_deadlocks": heatmap_wdeadlocks})

        return pd.DataFrame(heatmaps)
