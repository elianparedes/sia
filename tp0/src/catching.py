from .pokemon import Pokemon
from .pokeball import BasePokeball, PokeBall, UltraBall, FastBall, HeavyBall
from typing import Tuple
import random
import numpy as np

_POKEBALL = {
    "pokeball": lambda x: PokeBall(x),
    "ultraball": lambda x: UltraBall(x),
    "fastball": lambda x: FastBall(x),
    "heavyball": lambda x: HeavyBall(x),
}


def attempt_catch(
    pokemon: Pokemon, pokeball_type: str, noise=0.0
) -> Tuple[bool, float]:
    """Simulates throwing a pokeball to catch a pokemon

    Parameters
    ----------
    pokemon::[Pokemon]
        The pokemon being caught
    pokeball::[str]
        The type of pokeball to use

    Returns
    -------
    attempt_success::bool
        Returns True if the pokemon was caught otherwise False

    capture_rate::float
        The probability of the pokemon being caught
    """
    if pokeball_type not in _POKEBALL:
        raise ValueError("Invalid pokeball type")

    # Instanciating pokeball with pokemon to catch
    pokeball: BasePokeball = _POKEBALL[pokeball_type.lower()](pokemon)

    max_hp = pokemon.max_hp
    curr_hp = pokemon.current_hp
    catch_rate = pokeball.catch_rate
    ball_rate = pokeball.ball_rate

    # Get the property value from the enum, value[0] would be the name
    status = pokemon.status_effect.value[1]

    numerator = 1 + (max_hp * 3 - curr_hp * 2) * catch_rate * ball_rate * status
    denominator = max_hp * 3

    noise_multiplier = np.random.normal(1, noise)
    if noise_multiplier < 0:
        noise_multiplier = 0

    capture_rate = round((numerator / denominator) / 256, 4) * noise_multiplier
    if (capture_rate > 1):
        capture_rate = 1

    return (random.uniform(0, 1) < capture_rate, capture_rate)
