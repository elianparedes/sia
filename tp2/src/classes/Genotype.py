from src.classes.stats.Agilidad import Agilidad
from src.classes.stats.Altura import Altura
from src.classes.stats.Fuerza import Fuerza
from src.classes.stats.Pericia import Pericia
from src.classes.stats.Resistencia import Resistencia
from src.classes.stats.Vida import Vida
from typing import List


class Genotype:

    def __init__(self, fuerza: float, agilidad: float, pericia: float, resistencia: float, vida: float, altura: float):
        # Instantiation of the genotype normalizing stats
        total = fuerza + agilidad + pericia + resistencia + vida
        percentage = 150 / total
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
