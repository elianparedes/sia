from abc import ABC

from Player import Player


class Guerrero(Player, ABC):

    def fitness(self):
        return 0.9 * super.ataque() + 0.1 * super.defensa()
