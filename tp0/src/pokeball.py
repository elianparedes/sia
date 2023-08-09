from abc import ABC

from .pokemon import Pokemon


# ABC denotes abstract class,  this is not instantiable
# Everything could extend from Pokeball in this case, but I wanted to showcase
# abstract classes :)
class BasePokeball(ABC):
    _ball_rate = 1
    _name = "BasePokeball"

    def __init__(self, catching_pkmn: Pokemon):
        self._catching_pkmn = catching_pkmn

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"{self._name} (ball_rate={self._ball_rate})"

    @property
    def ball_rate(self):
        return self._ball_rate

    @property
    def catch_rate(self):
        return self._catching_pkmn.catch_rate


class PokeBall(BasePokeball):
    def __init__(self, catching_pkmn: Pokemon):
        super().__init__(catching_pkmn)
        self._name = "Pokeball"


class UltraBall(BasePokeball):
    def __init__(self, catching_pkmn: Pokemon):
        super().__init__(catching_pkmn)
        self._name = "Ultraball"
        self._ball_rate = 2


class FastBall(BasePokeball):
    def __init__(self, catching_pkmn: Pokemon):
        super().__init__(catching_pkmn)
        self._name = "FastBall"

    # This pokeball affects the catch rate based on the pokemon's speed
    @property
    def catch_rate(self):
        modifier = 1
        if self._catching_pkmn.stats.speed >= 100:
            modifier = 4

        return modifier * self._catching_pkmn.catch_rate


class HeavyBall(BasePokeball):
    def __init__(self, catching_pkmn: Pokemon):
        super().__init__(catching_pkmn)
        self._name = "HeavyBall"

    # This pokeball affects the catch rate based on the pokemon's weight
    @property
    def catch_rate(self):
        modifier = -20
        if self._catching_pkmn.weight > 451.5:
            modifier = 20
        if self._catching_pkmn.weight > 677.3:
            modifier = 30
        if self._catching_pkmn.weight > 903:
            modifier = 40

        catch_rate = self._catching_pkmn.catch_rate + modifier

        return catch_rate if catch_rate > 0 else 1
