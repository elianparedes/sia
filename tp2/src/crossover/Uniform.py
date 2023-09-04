from src.classes.Genotype import Genotype
from src.crossover.CrossoverABC import CrossoverABC
import random


class Uniform(CrossoverABC):

    @classmethod
    def cross(cls, gene1: Genotype, gene2: Genotype) -> tuple[Genotype, Genotype]:
        gene1_arr = gene1.to_array()
        gene2_arr = gene2.to_array()
        child1 = gene1_arr
        child2 = gene2_arr
        for i in range(len(gene1_arr)):
            if random.random() < 0.5:
                child1[i], child2[i] = child2[i], child1[i]

        return Genotype.from_array(child1), Genotype.from_array(child2)
