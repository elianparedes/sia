from src.classes.characters.CharacterABC import CharacterABC

ATK_PERCENT = 0.9
DEF_PERCENT = 0.1


class Archer(CharacterABC):

    def __init__(self, gene):
        super().__init__(gene, ATK_PERCENT, DEF_PERCENT)

    def __str__(self):
        return 'Archer: ' + super().__str__()
