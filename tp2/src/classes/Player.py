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
        return (self.gene.get_agility().get_p() + self.gene.get_intelligence().get_p()) * self.gene.get_strength().get_p() * self.gene.get_height().get_ATM()

    def defensa(self):
        return (self.gene.get_endurance().get_p() + self.gene.get_intelligence().get_p()) * self.gene.get_health().get_p() * self.gene.get_height().get_DEM()

    def __str__(self):
        return self.gene.__str__()

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented

        return self.gene == other.gene


