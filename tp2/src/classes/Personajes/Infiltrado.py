from abc import ABC

from Player import Player


class Infiltrado(Player, ABC):

    def fitness(self):
        return 0.8 * super.ataque() + 0.3 * super.defensa()
