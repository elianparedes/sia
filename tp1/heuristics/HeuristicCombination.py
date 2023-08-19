from heuristics.HeuristicABC import HeuristicABC


class HeuristicCombination(HeuristicABC):
    @classmethod
    def calculate(cls, state, *argv: HeuristicABC) -> int:
        return max(heuristic.calculate(state) for heuristic in argv)
