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

print("Wall positions:", parsed_positions.get('wall', []))
print("Player position:", parsed_positions.get('player', []))
print("Goal positions:", parsed_positions.get('goal', []))
print("Box positions:", parsed_positions.get('box', []))
print("Box on goal positions:", parsed_positions.get('box_on_goal', []))


walls = parsed_positions.get('wall', [])
blanks = parsed_positions.get('blank', [])
boxes = parsed_positions.get('box', [])
player = parsed_positions.get('player', [])[0]
goals = parsed_positions.get('goal', [])
deadlocks = SokobanUtils.get_deadlocks(walls, blanks)

print("Deadlock positions:", deadlocks)

#BFS.bfs(State(parsed_positions.get('box', []), parsed_positions.get('wall', []), parsed_positions.get('player', [])[0], parsed_positions.get('goal', []), []))
BFS.bfs(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#AStarSearch.a_star_search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
#LocalGreedy.local_greedy(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))
