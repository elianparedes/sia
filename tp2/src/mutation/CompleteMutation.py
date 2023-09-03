from src.mutation.MutationABC import MutationABC
from src.classes.Genotipo import Genotipo
import random


class CompleteMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotipo, probability: float) -> Genotipo | None:
        new_genes = genes.to_array()

        if random.uniform(0, 1) <= probability:
            for i in range(len(genes)):
                # Mutation
                stat = genes[i].mutate()

                # Search and replace with mutated gene
                new_genes[i] = stat
        return Genotipo.from_array(new_genes)
