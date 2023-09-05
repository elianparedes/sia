from src.selection.ProbabilisticTournament import ProbabilisticTournament
from src.selection.DeterministicTournament import DeterministicTournament
from src.selection.Elite import Elite
from src.selection.Boltzmann import Boltzmann
from src.selection.Ranked import Ranked
from src.selection.Roulette import Roulette
from src.selection.Universal import Universal


class SelectionFactory:
    SELECTION_CLASSES = {
        "probabilistic": ProbabilisticTournament,
        "deterministic": DeterministicTournament,
        "elite": Elite,
        "boltzmann": Boltzmann,
        "ranked": Ranked,
        "roulette": Roulette,
        "universal": Universal
    }

    @classmethod
    def configure(cls, method_name, **kwargs):
        if method_name not in cls.SELECTION_CLASSES:
            raise ValueError(f"Unknown selection method: {method_name}")
        selection_class = cls.SELECTION_CLASSES[method_name]
        selection_class.configure(**kwargs)
        return selection_class
