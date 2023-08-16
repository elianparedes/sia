from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.LocalGreedy import LocalGreedy
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
# BFS.bfs(State(parsed_positions.get('box', []), parsed_positions.get('wall', []), parsed_positions.get('player', [])[0], parsed_positions.get('goal', []), []))
DFS.dfs(State(set(parsed_positions.get('box', [])), set(parsed_positions.get('wall', [])),
              parsed_positions.get('player', [])[0], set(parsed_positions.get('goal', [])), []))
# LocalGreedy.local_greedy(State(parsed_positions.get('box', []), parsed_positions.get('wall', []), parsed_positions.get('player', [])[0], parsed_positions.get('goal', []), []))
