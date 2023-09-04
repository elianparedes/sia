from src.classes.Player import Player


class Defensor(Player):

    def fitness(self):
        return 0.1 * super().ataque() + 0.9 * super().defensa()

    def __str__(self):
        return 'Defensor: ' + super().__str__()
