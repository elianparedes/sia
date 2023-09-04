from src.classes.genes.Agility import Agility
from src.classes.genes.Height import Height
from src.classes.genes.Strength import Strength
from src.classes.genes.Intelligence import Intelligence
from src.classes.genes.Endurance import Endurance
from src.classes.genes.Health import Health
from typing import List


class Genotype:

    def __init__(self, strength: float, agility: float, intelligence: float, endurance: float, health: float, height: float):
        # Instantiation of the genotype normalizing genes
        total = strength + agility + intelligence + endurance + health
        percentage = 150 / total
        self.strength = Strength(strength * percentage)
        self.agility = Agility(agility * percentage)
        self.intelligence = Intelligence(intelligence * percentage)
        self.endurance = Endurance(endurance * percentage)
        self.health = Health(health * percentage)
        self.height = Height(height)

    def get_strength(self) -> Strength:
        return self.strength

    def get_agility(self) -> Agility:
        return self.agility

    def get_intelligence(self) -> Intelligence:
        return self.intelligence

    def get_endurance(self) -> Endurance:
        return self.endurance

    def get_health(self) -> Health:
        return self.health

    def get_height(self) -> Height:
        return self.height

    def set_agility(self, agility):
        self.agility = agility

    def set_strength(self, strength):
        self.strength = strength

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence

    def set_endurance(self, endurance):
        self.endurance = endurance

    def set_health(self, health):
        self.health = health

    def set_height(self, height):
        self.height = height

    @staticmethod
    def from_array(arr: List[float]):
        return Genotype(*arr)

    def to_array(self) -> [float, float, float, float, float, float]:
        return [self.strength.value, self.agility.value, self.intelligence.value, self.endurance.value, self.health.value, self.height.value]

    def __str__(self):
        return f'Gene(strength={self.strength}, agility={self.agility}, intelligence={self.intelligence}, ' \
               f'endurance={self.endurance}, health={self.health}, height={self.height})'

    def __eq__(self, other):
        if not isinstance(other, Genotype):
            return NotImplemented

        return (self.strength == other.strength) and (self.height == other.height) \
               and (self.health == other.health) and (self.endurance == other.endurance) \
               and (self.agility == other.agility) and (self.intelligence == other.intelligence)
