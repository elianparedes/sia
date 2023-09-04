from src.mutation.MutationABC import MutationABC
from src.classes.Genotype import Genotype
import random


class UniformMultigeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        new_genes = genes.to_array()

        for i in range(len(genes)):
            if random.uniform(0, 1) <= probability:
                # Mutation
                stat = genes[i].mutate()

                # Search and replace with mutated gene
                new_genes[i] = stat
        return Genotype.from_array(new_genes)
    