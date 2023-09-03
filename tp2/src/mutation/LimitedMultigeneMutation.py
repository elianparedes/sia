from src.mutation.MutationABC import MutationABC
from src.classes.Genotipo import Genotipo
import random


class LimitedMultigeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotipo, probability: float) -> Genotipo | None:
        shuffled_genes = genes.to_array()
        new_genes = genes.to_array()
        random.shuffle(shuffled_genes)

        # Random selection of the first M genes
        mutation_amount = random.randint(1, len(genes))
        for i in range(mutation_amount):
            if random.uniform(0, 1) <= probability:
                # Mutation
                stat = shuffled_genes[i].mutate()

                # Search and replace with mutated gene
                index = new_genes.index(shuffled_genes[i])
                new_genes[index] = stat
        return Genotipo.from_array(new_genes)
