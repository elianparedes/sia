from src.mutation.MutationABC import MutationABC
from src.classes.Genotype import Genotype
import random


class CompleteMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        new_genes = genes.to_array()

        if random.uniform(0, 1) <= probability:
            for i in range(len(new_genes)):
                # Mutation
                stat = new_genes[i].mutate()

                # Search and replace with mutated gene
                new_genes[i] = stat
        return Genotype.from_array(new_genes)
