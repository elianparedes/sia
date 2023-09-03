from src.mutation.MutationABC import MutationABC
from src.classes.Genotipo import Genotipo
import random


class SingleGeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotipo, probability: float) -> Genotipo | None:
        shuffled_genes = genes.to_array()
        new_genes = genes.to_array()
        random.shuffle(shuffled_genes)
        if random.uniform(0, 1) <= probability:
            # Mutation
            stat = shuffled_genes[0].mutate()

            # Search and replace with mutated gene
            index = new_genes.index(shuffled_genes[0])
            new_genes[index] = stat
        return Genotipo.from_array(new_genes)
