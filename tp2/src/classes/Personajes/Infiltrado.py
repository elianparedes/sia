from src.classes.Player import Player


class Infiltrado(Player):

    def fitness(self):
        return 0.8 * super.ataque() + 0.3 * super.defensa()
