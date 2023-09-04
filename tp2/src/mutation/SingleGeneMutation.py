from src.mutation.MutationABC import MutationABC
from src.classes.Genotype import Genotype
import random


class SingleGeneMutation(MutationABC):

    @classmethod
    def mutate(cls, genes: Genotype, probability: float) -> Genotype | None:
        new_genes = genes.to_array()
        if random.uniform(0, 1) <= probability:
            # Random selection of the gene to mutate
            rand = random.randint(0, len(new_genes) - 1)
            # check if it is the height gene
            if rand == (len(new_genes) - 1):
                # Search and replace with mutated gene
                new_genes[rand] = random.uniform(1.3, 2.0)
            else:
                # Search and replace with mutated gene
                new_genes[rand] = random.uniform(0, 150)
        return Genotype.from_array(new_genes)
