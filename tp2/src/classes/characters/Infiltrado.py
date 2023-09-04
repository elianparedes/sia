from src.classes.Player import Player


class Infiltrado(Player):

    def fitness(self):
        return 0.8 * super().ataque() + 0.3 * super().defensa()

    def __str__(self):
        return 'Infiltrado: ' + super().__str__()
