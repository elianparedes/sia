from enum import Enum
from typing import NamedTuple, Tuple
import math
import json


class Type(str, Enum):
    NORMAL = "normal"
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"
    ICE = "ice"
    FIGHTING = "fighting"
    POISON = "poison"
    GROUND = "ground"
    FLYING = "flying"
    PSYCHIC = "psychic"
    BUG = "bug"
    ROCK = "rock"
    GHOST = "ghost"
    DARK = "dark"
    DRAGON = "dragon"
    STEEL = "steel"
    FAIRY = "fairy"
    NONE = "none"


class Stats(NamedTuple):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class StatusEffect(Enum):
    POISON = ("poison", 1.5)
    BURN = ("burn", 1.5)
    PARALYSIS = ("paralysis", 1.5)
    SLEEP = ("sleep", 2)
    FREEZE = ("freeze", 2)
    NONE = ("none", 1)


class Pokemon:
    def __init__(
        self,
        name: str,
        type: Tuple[Type, Type],
        current_hp: int,
        status_effect: StatusEffect,
        level: int,
        stats: Stats,
        catch_rate: int,
        weight: float,
    ):

        self._name = name  # Underscored variables denote "private"
        self._type = type
        self._stats = stats
        self._catch_rate = catch_rate
        self._weight = weight

        self.current_hp = current_hp
        self.status_effect = status_effect
        self.level = level

    @property  # Property annotation for read-only attributes
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def stats(self):
        return self._stats

    @property
    def catch_rate(self):
        return self._catch_rate

    @property
    def weight(self):
        return self._weight

    @property
    def max_hp(self):
        base_hp = self._stats.hp
        level = self.level

        # Real max hp formula includes EVs and IVs, this is a simplification
        return math.floor(0.01 * (2 * base_hp) + level + 10)


class PokemonFactory:
    def __init__(self, src_file="pokemon.json"):
        self._src_file = src_file

    def create(
        self, name: str, level: int, status: StatusEffect, hp_percentage: float
    ) -> Pokemon:
        if (hp_percentage < 0 or hp_percentage > 1):
            raise ValueError("hp has to be value between 0 and 1")
        with open(self._src_file, "r") as c:
            pokemon_db = json.load(c)
            if name.lower() not in pokemon_db:
                raise ValueError("Not a valid pokemon")
            poke = pokemon_db[name]

            t1, t2 = poke["type"]
            type = (Type(t1.lower()), Type(t2.lower()))
            stats = Stats(*poke["stats"])

            new_pokemon = Pokemon(
                name, type, 0, status, level, stats, poke["catch_rate"], poke["weight"]
            )

            max_hp = new_pokemon.max_hp
            hp = math.floor(hp_percentage * max_hp)
            new_pokemon.current_hp = hp if hp > 0 else 1
            return new_pokemon
