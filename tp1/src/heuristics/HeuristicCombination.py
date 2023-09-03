from src.heuristics.HeuristicABC import HeuristicABC
from src.heuristics.ManhattanDistance import ManhattanDistance
from src.heuristics.MinDistance import MinDistance
from src.heuristics.BipartiteHeuristic import BipartiteHeuristic

class HeuristicCombination(HeuristicABC):
    @classmethod
    def calculate(cls, state) -> int:
        return max(MinDistance.calculate(state), ManhattanDistance.calculate(state), BipartiteHeuristic.calculate(state))
