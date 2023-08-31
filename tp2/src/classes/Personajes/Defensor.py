from abc import ABC

from Player import Player


class Defensor(Player, ABC):

    def fitness(self):
        return 0.1 * super.ataque() + 0.9 * super.defensa()