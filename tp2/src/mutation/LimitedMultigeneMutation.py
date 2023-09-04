from src.mutation.MutationABC import MutationABC
from src.classes.Genotype import Genotype
import random


class LimitedMultigeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        shuffled_genes = genes.to_array()
        new_genes = genes.to_array()
        random.shuffle(shuffled_genes)

        # Random selection of the first M genes
        mutation_amount = random.randint(1, len(new_genes))
        for i in range(mutation_amount):
            if random.uniform(0, 1) <= probability:
                # Mutation
                stat = shuffled_genes[i].mutate()

                # Search and replace with mutated gene
                index = new_genes.index(shuffled_genes[i])
                new_genes[index] = stat
        return Genotype.from_array(new_genes)
