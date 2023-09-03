from src.mutation.MutationABC import MutationABC
from src.classes.Genotipo import Genotipo
import random


class UniformMultigeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotipo, probability: float) -> Genotipo | None:
        new_genes = genes.to_array()

        for i in range(len(genes)):
            if random.uniform(0, 1) <= probability:
                # Mutation
                stat = genes[i].mutate()

                # Search and replace with mutated gene
                new_genes[i] = stat
        return Genotipo.from_array(new_genes)
    