from src.selection.SelectionABC import SelectionABC


class EliteSelection(SelectionABC):

    @classmethod
    def select(cls, population: [], individuals: int):
        new_population = []
        sorted_population = sorted(population, reverse=True)
        i = 0
        k = 0
        while i != individuals:
            new_population.append(sorted_population[k])
            i += 1
            k += 1
            if k == len(sorted_population):
                k = 0
        return new_population
