import random

from src.crossover.CrossoverABC import CrossoverABC
from src.classes.Genotype import Genotype


class TwoPoint(CrossoverABC):
    @classmethod
    def cross(cls, gene1: Genotype, gene2: Genotype) -> tuple[Genotype, Genotype]:
        gene1_arr = gene1.to_array()
        gene2_arr = gene2.to_array()

        last_gene_index = len(gene1_arr) - 1

        first_point = random.randrange(0, last_gene_index - 1)
        second_point = random.randrange(first_point + 1, last_gene_index)

        child1 = gene1_arr[:first_point] + gene2_arr[first_point:second_point] + gene1_arr[second_point:]
        child2 = gene2_arr[:first_point] + gene1_arr[first_point:second_point] + gene2_arr[second_point:]

        return Genotype.from_array(child1), Genotype.from_array(child2)
