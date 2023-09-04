from abc import ABC


class CharacterABC(ABC):

    def __init__(self, gene, attack_percent, defense_percent):
        self.gene = gene
        self.attack_percent = attack_percent
        self.defense_percent = defense_percent

    def get_gene(self):
        return self.gene

    def fitness(self):
        return self.attack_percent * self.attack() + self.defense_percent * self.defense()

    def attack(self):
        return (self.gene.get_agility().get_p() + self.gene.get_intelligence().get_p()) * self.gene.get_strength().get_p() \
               * self.gene.get_height().get_ATM()

    def defense(self):
        return (self.gene.get_endurance().get_p() + self.gene.get_intelligence().get_p()) * self.gene.get_health().get_p() \
               * self.gene.get_height().get_DEM()

    def __str__(self):
        return self.gene.__str__()

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CharacterABC):
            return NotImplemented

        return self.gene == other.gene
