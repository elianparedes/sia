from src.classes.stats.Agility import Agility
from src.classes.stats.Height import Height
from src.classes.stats.Strength import Strength
from src.classes.stats.Intelligence import Intelligence
from src.classes.stats.Endurance import Endurance
from src.classes.stats.Health import Health
from typing import List


class Genotype:

    def __init__(self, strength: float, agility: float, intelligence: float, endurance: float, health: float, height: float):
        # Instantiation of the genotype normalizing stats
        total = strength + agility + intelligence + endurance + health
        percentage = 150 / total
        self.fuerza = Strength(strength * percentage)
        self.agilidad = Agility(agility * percentage)
        self.pericia = Intelligence(intelligence * percentage)
        self.resistencia = Endurance(endurance * percentage)
        self.vida = Health(health * percentage)
        self.altura = Height(height)

    def get_strength(self) -> Strength:
        return self.fuerza

    def get_agility(self) -> Agility:
        return self.agilidad

    def get_intelligence(self) -> Intelligence:
        return self.pericia

    def get_endurance(self) -> Endurance:
        return self.resistencia

    def get_health(self) -> Health:
        return self.vida

    def get_height(self) -> Height:
        return self.altura

    def set_agility(self, agilidad):
        self.agilidad = agilidad

    def set_strength(self, fuerza):
        self.fuerza = fuerza

    def set_intelligence(self, pericia):
        self.pericia = pericia

    def set_endurance(self, resistencia):
        self.resistencia = resistencia

    def set_health(self, vida):
        self.vida = vida

    def set_height(self, altura):
        self.altura = altura

    @staticmethod
    def from_array(arr: List[float]):
        return Genotype(*arr)

    def to_array(self) -> [float, float, float, float, float, float]:
        return [self.fuerza.value, self.agilidad.value, self.pericia.value, self.resistencia.value, self.vida.value, self.altura.value]

    def __str__(self):
        return f'Gene(fuerza={self.fuerza}, agilidad={self.agilidad}, pericia={self.pericia}, resistencia={self.resistencia}, vida={self.vida}, altura={self.altura})'

    def __eq__(self, other):
        if not isinstance(other, Genotype):
            return NotImplemented

        return (self.fuerza == other.fuerza) and (self.altura == other.altura) \
            and (self.vida == other.vida) and (self.resistencia == other.resistencia) \
            and (self.agilidad == other.agilidad) and (self.pericia == other.pericia)
