from src.classes.Player import Player

ATK_PERCENT = 0.9
DEF_PERCENT = 0.1

class Arquero(Player):

    def fitness(self):
        return ATK_PERCENT * super().ataque() + DEF_PERCENT * super().defensa()

    def __str__(self):
        return 'Archer: ' + super().__str__()

