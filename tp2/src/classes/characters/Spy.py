from src.classes.Player import Player

ATK_PERCENT = 0.8
DEF_PERCENT = 0.3

class Spy(Player):

    def fitness(self):
        return ATK_PERCENT * super().ataque() + DEF_PERCENT * super().defensa()

    def __str__(self):
        return 'Spy: ' + super().__str__()
