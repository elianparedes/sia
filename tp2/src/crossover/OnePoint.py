from src.classes.Genotype import Genotype
from src.crossover.CrossoverABC import CrossoverABC
import random


class OnePoint(CrossoverABC):
    @classmethod
    def cross(cls, gene1: Genotype, gene2: Genotype) -> tuple[Genotype, Genotype]:
        gene1_arr = gene1.to_array()
        gene2_arr = gene2.to_array()
        genes_count = len(gene1_arr)
        locus = random.randrange(1, genes_count)
        child1 = gene1_arr[:locus] + gene2_arr[locus:]
        child2 = gene2_arr[:locus] + gene1_arr[locus:]

        return Genotype.from_array(child1), Genotype.from_array(child2)
