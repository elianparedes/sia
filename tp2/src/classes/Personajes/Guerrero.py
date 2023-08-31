from abc import ABC

from Player import Player


class Guerrero(Player, ABC):

    def fitness(self):
        return 0.6 * super.ataque() + 0.4 * super.defensa()
