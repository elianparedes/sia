from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.LocalGreedy import LocalGreedy
from algorithms.AStarSearch import AStarSearch
from classes.SokobanUtils import SokobanUtils
from classes.State import State

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
deadlocks = SokobanUtils.get_deadlocks(walls, blanks)


print("Wall positions:", walls)
print("Player position:", player)
print("Goal positions:", goals)
print("Box positions:", boxes)
print("Box on goal positions:", parsed_positions.get('box_on_goal', []))
print("Deadlock positions:", deadlocks)

#DFS.dfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#BFS.bfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#AStarSearch.a_star_search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#LocalGreedy.local_greedy(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
