from src.selection.SelectionFactory import SelectionFactory
from src.classes.Genotype import Genotype
from src.classes.characters.Spy import Spy

# This test is just a demonstration of how to use SelectionFactory with config maps

config = {"probabilistic_tournament": {},
          "deterministic_tournament": {"size": 2},
          "elite": {},
          "boltzmann": {"t0": 10, "tc": 5, "k": 2, "generation": 10},
          "ranked": {},
          "roulette": {},
          "universal": {}
          }

population = [Spy(Genotype.from_array([10, 20, 30, 40, 50, 1])),
              Spy(Genotype.from_array([20, 30, 40, 50, 10, 1])),
              Spy(Genotype.from_array([30, 40, 50, 10, 20, 1])),
              Spy(Genotype.from_array([40, 50, 10, 20, 30, 1]))]

for method_name, settings in config.items():
    selection = SelectionFactory.configure(method_name, **settings)
    children = selection.select(population, 2)
    print(method_name + ' ' + str(children[0]) + ' ' + str(children[1]))
