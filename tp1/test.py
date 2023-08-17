from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.LocalGreedy import LocalGreedy
from algorithms.AStarSearch import AStarSearch
from classes.SokobanUtils import SokobanUtils
from classes.StateUtils import StateUtils
from classes.StateBuilder import StateBuilder
from classes.State import State
import time

# Example Sokoban board
# sokoban_board = """
# #########
# #@$.##
# #########
# """
sokoban_board = """
  ##### 
###   # 
#.@$  # 
### $.# 
#.##$ # 
# # . ##
#$ *$$.#
#   .  #
########
"""
parsed_positions = SokobanUtils.parse_sokoban_board(sokoban_board)

walls = parsed_positions.get('wall', [])
blanks = parsed_positions.get('blank', [])
boxes = parsed_positions.get('box', [])
player = parsed_positions.get('player', [])[0]
goals = parsed_positions.get('goal', [])
deadlocks = StateUtils.obtain_deadlocks(walls, goals)


print("Wall positions:", walls)
print("Player position:", player)
print("Goal positions:", goals)
print("Box positions:", boxes)
print("Box on goal positions:", parsed_positions.get('box_on_goal', []))
print("Deadlock positions:", deadlocks)
builder = StateBuilder(max(point.x for point in walls) + 1, max(point.y for point in walls) + 1)
builder.add_points(walls, '#').add_points(deadlocks, 'x').add_points(goals, 'o')
grid = builder.build()
builder.print_grid()

#BFS.bfs(State(parsed_positions.get('box', []), parsed_positions.get('wall', []), parsed_positions.get('player', [])[0], parsed_positions.get('goal', []), []))
start_time = time.time()
BFS.bfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#DFS.dfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#AStarSearch.a_star_search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#LocalGreedy.local_greedy(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to execute the algorithm: {elapsed_time:.6f} seconds")