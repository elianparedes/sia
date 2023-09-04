from src.classes.Player import Player


class Warrior(Player):

    def fitness(self):
        return 0.6 * super().ataque() + 0.4 * super().defensa()

    def __str__(self):
        return 'Warrior: ' + super().__str__()

