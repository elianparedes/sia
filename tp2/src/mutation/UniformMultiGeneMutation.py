from src.mutation.MutationABC import MutationABC
from src.classes.Genotype import Genotype
import random


class UniformMultigeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        new_genes = genes.to_array()
        for i in range(len(new_genes)):
            if random.uniform(0, 1) <= probability:
                # check if it is the height gene
                if i == (len(new_genes) - 1):
                    # Search and replace with mutated gene
                    new_genes[i] = random.uniform(1.3, 2.0)
                else:
                    # Search and replace with mutated gene
                    new_genes[i] = random.uniform(0, 150)
        return Genotype.from_array(new_genes)
