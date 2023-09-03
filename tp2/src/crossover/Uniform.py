from src.crossover.CrossoverABC import CrossoverABC
from src.classes.Gene import Gene
import random


class Uniform(CrossoverABC):

    @classmethod
    def cross(cls, gene1: Gene, gene2: Gene) -> tuple[Gene, Gene]:
        gene1_arr = gene1.to_array()
        gene2_arr = gene2.to_array()
        child1 = gene1_arr
        child2 = gene2_arr
        for i in range(len(gene1_arr)):
            if random.random() < 0.5:
                child1[i], child2[i] = child2[i], child1[i]

        return tuple([Gene.from_array(child1), Gene.from_array(child2)])
