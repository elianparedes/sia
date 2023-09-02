from src.classes.Player import Player


class Arquero(Player):

    def fitness(self):
        return 0.9 * super.ataque() + 0.1 * super.defensa()
