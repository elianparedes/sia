from src.classes.characters.CharacterABC import CharacterABC

ATK_PERCENT = 0.8
DEF_PERCENT = 0.3


class Spy(CharacterABC):

    def __init__(self, gene):
        super().__init__(gene, ATK_PERCENT, DEF_PERCENT)

    def __str__(self):
        return 'Spy: ' + super().__str__()
