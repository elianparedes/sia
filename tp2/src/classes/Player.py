from abc import ABC, abstractmethod


class Player(ABC):

    @abstractmethod
    def fitness(self):
        pass

    def __init__(self, gene):
        self.gene = gene

    def get_gene(self):
        return self.gene

    def ataque(self):
        return (self.gene.get_agilidad().get_p() + self.gene.get_pericia().get_p()) * self.gene.get_fuerza().get_p() * self.gene.get_altura().get_ATM()

    def defensa(self):
        return (self.gene.get_resistencia().get_p() + self.gene.get_pericia().get_p()) * self.gene.get_vida().get_p() * self.gene.get_altura().get_DEM()

    def __str__(self):
        return self.gene.__str__()
