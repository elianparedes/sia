from heuristics.HeuristicABC import HeuristicABC


class HeuristicsCombination:
    @classmethod
    def calculate(cls, state, heuristic_1, heuristic_2):
        return max(heuristic_1.calculate(state), heuristic_2.calculate(state))
