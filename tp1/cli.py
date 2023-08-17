import sys
import os
import time

from algorithms.AStarSearch import AStarSearch
from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.LocalGreedy import LocalGreedy
from classes.SokobanUtils import SokobanUtils
from classes.State import State

# Argument constants
ARG_TIME = "time"
ARG_DEADLOCKS = "deadlocks"
ARG_MAP = "map"
ARG_ALGORITHM = "algorithm"
ARG_HELP = "help"

ALGORITHMS = ["bfs", "dfs", "locgreedy", "astar"]


def show_greeting(args, map_contents):
    print("Algorithm: ", args[ARG_ALGORITHM])
    print("Deadlocks? ", args[ARG_DEADLOCKS])
    print("Show time? ", args[ARG_TIME])
    print("Map: ", args[ARG_MAP])
    print(map_contents)
    print("\nAny minute now...")


def show_help():
    print("Usage: python my_script.py -a <algorithm> -m <map_name> [-t] [-d] [-h]")
    print(f"-a, --{ARG_ALGORITHM}")
    formatted_algorithms = ", ".join([f"'{algorithm}'" for algorithm in ALGORITHMS])
    print(f"\tCan be any of: {formatted_algorithms}")
    print(f"-m, --{ARG_MAP}")
    print("\tThe name of a map (without the suffix .txt) inside the resources/maps folder")
    print(f"-t, --{ARG_TIME}")
    print("\tShows elapsed time")
    print(f"-d, --{ARG_DEADLOCKS}")
    print("\tChecks for deadlocks before running the algorithm")
    print(f"-h, --{ARG_HELP}")
    print("\tYou just typed it!")
    return


def open_map(map_path):
    try:
        with open(map_path, "r") as map_file:
            map_contents = map_file.read()
    except FileNotFoundError:
        print(f"Map '{map_path}' not found.")
        print("Make sure it is under the resources/maps folder.")
        exit(1)

    return map_contents


def execute_algorithm(parsed_positions, algorithm, wants_deadlocks):
    walls = parsed_positions.get('wall', [])
    blanks = parsed_positions.get('blank', [])
    boxes = parsed_positions.get('box', [])
    player = parsed_positions.get('player', [])[0]
    goals = parsed_positions.get('goal', [])
    deadlocks = []
    if wants_deadlocks is True:
        deadlocks = SokobanUtils.get_deadlocks(walls, blanks)

    if algorithm.lower() == "locgreedy":
        LocalGreedy.local_greedy(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
    elif algorithm.lower() == "dfs":
        DFS.dfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
    elif algorithm.lower() == "astar":
        AStarSearch.a_star_search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
    elif algorithm.lower() == "bfs":
        BFS.bfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
    else:
        print("Not a known algorithm.")
        print("Options are: bfs, dfs, astar, locgreedy.")
        exit(1)

    return


def main():
    args = {ARG_ALGORITHM: None, ARG_MAP: None, ARG_HELP: False, ARG_TIME: False, ARG_DEADLOCKS: False}

    # Parse command-line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg in ("-a", "--algorithm"):
            i += 1
            args[ARG_ALGORITHM] = sys.argv[i] if i < len(sys.argv) else None
        elif arg in ("-m", "--map"):
            i += 1
            args[ARG_MAP] = sys.argv[i] if i < len(sys.argv) else None
        elif arg in ("-h", "--help"):
            args[ARG_HELP] = True
        elif arg in ("-t", "--time"):
            args[ARG_TIME] = True
        elif arg in ("-d", "--deadlocks"):
            args[ARG_DEADLOCKS] = True

        i += 1

    # Your main script logic here
    algorithm = args[ARG_ALGORITHM]
    map_name = args[ARG_MAP]
    help_flag = args[ARG_HELP]
    show_time = args[ARG_TIME]
    deadlocks = args[ARG_DEADLOCKS]

    if len(sys.argv) == 1 or help_flag:
        show_help()
        exit(0)
    else:
        if args[ARG_ALGORITHM] is None or args[ARG_MAP] is None:
            print("Incorrect usage.")
            print("Type 'python cli.py -h' to get more help.")
            exit(1)
        elif args[ARG_ALGORITHM] not in ALGORITHMS:
            print("Not a known algorithm.")

        map_path = os.path.join(".", "resources", "maps", f"{map_name}.txt")
        map_contents = open_map(map_path)
        parsed_contents = SokobanUtils.parse_sokoban_board(map_contents)
        show_greeting(args, map_contents)
        if show_time is True:
            start_time = time.time()
            execute_algorithm(parsed_contents, algorithm, deadlocks)
            elapsed_time = time.time() - start_time
            print(f"Elapsed time: {elapsed_time:.6f} seconds")
        else:
            execute_algorithm(parsed_contents, algorithm, deadlocks)


if __name__ == "__main__":
    main()
