from src.classes.characters.CharacterABC import CharacterABC

ATK_PERCENT = 0.1
DEF_PERCENT = 0.9


class Defender(CharacterABC):

    def __init__(self, gene):
        super().__init__(gene, ATK_PERCENT, DEF_PERCENT)

    def __str__(self):
        return 'Defender: ' + super().__str__()
