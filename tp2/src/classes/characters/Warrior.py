from src.classes.characters.CharacterABC import CharacterABC

ATK_PERCENT = 0.6
DEF_PERCENT = 0.4


class Warrior(CharacterABC):

    def __init__(self, gene):
        super().__init__(gene, ATK_PERCENT, DEF_PERCENT)

    def __str__(self):
        return 'Warrior: ' + super().__str__()

