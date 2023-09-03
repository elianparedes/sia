from src.classes.Stats.Agilidad import Agilidad
from src.classes.Stats.Altura import Altura
from src.classes.Stats.Fuerza import Fuerza
from src.classes.Stats.Pericia import Pericia
from src.classes.Stats.Resistencia import Resistencia
from src.classes.Stats.Vida import Vida
from typing import List

class Genotipo:

    def __init__(self, fuerza: float, agilidad: float, pericia: float, resistencia: float, vida: float, altura: float):
        # Instantiation of the genotype normalizing stats
        sum = fuerza + agilidad + pericia + resistencia + vida
        percentage = 150 / sum
        self.fuerza = Fuerza(fuerza * percentage)
        self.agilidad = Agilidad(agilidad * percentage)
        self.pericia = Pericia(pericia * percentage)
        self.resistencia = Resistencia(resistencia * percentage)
        self.vida = Vida(vida * percentage)
        self.altura = Altura(altura)


    def get_fuerza(self) -> Fuerza:
        return self.fuerza

    def get_agilidad(self) -> Agilidad:
        return self.agilidad

    def get_pericia(self) -> Pericia:
        return self.pericia

    def get_resistencia(self) -> Resistencia:
        return self.resistencia

    def get_vida(self) -> Vida:
        return self.vida

    def get_altura(self) -> Altura:
        return self.altura

    def set_agilidad(self, agilidad):
        self.agilidad = agilidad

    def set_fuerza(self, fuerza):
        self.fuerza = fuerza

    def set_pericia(self, pericia):
        self.pericia = pericia

    def set_resistencia(self, resistencia):
        self.resistencia = resistencia

    def set_vida(self, vida):
        self.vida = vida

    def set_altura(self, altura):
        self.altura = altura

    @staticmethod
    def from_array(arr: List[float]):
        return Genotipo(*arr)

    def to_array(self) -> [Fuerza, Agilidad, Pericia, Resistencia, Vida, Altura]:
        return [self.fuerza, self.agilidad, self.pericia, self.resistencia, self.vida, self.altura]

    def __str__(self):
        return f'Gene(fuerza={self.fuerza}, agilidad={self.agilidad}, pericia={self.pericia}, resistencia={self.resistencia}, vida={self.vida}, altura={self.altura})'

    def __eq__(self, other):
        if not isinstance(other, Genotipo):
            return NotImplemented

        return (self.fuerza == other.fuerza) and (self.altura == other.altura) \
               and (self.vida == other.vida) and (self.resistencia == other.resistencia) \
               and (self.agilidad == other.agilidad) and (self.pericia == other.pericia)
