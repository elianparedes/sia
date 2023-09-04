from src.classes.Player import Player


class Defender(Player):

    def fitness(self):
        return 0.1 * super().ataque() + 0.9 * super().defensa()

    def __str__(self):
        return 'Defender: ' + super().__str__()
