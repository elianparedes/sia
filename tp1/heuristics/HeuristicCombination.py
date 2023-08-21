from heuristics.HeuristicABC import HeuristicABC
from heuristics.ManhattanDistance import ManhattanDistance
from heuristics.MinDistance import MinDistance
from heuristics.BipartiteHeuristic import BipartiteHeuristic

class HeuristicCombination(HeuristicABC):
    @classmethod
    def calculate(cls, state) -> int:
        return max(MinDistance.calculate(state), ManhattanDistance.calculate(state), BipartiteHeuristic.calculate(state))
