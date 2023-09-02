from src.classes.Player import Player


class Defensor(Player):

    def fitness(self):
        return 0.1 * super.ataque() + 0.9 * super.defensa()