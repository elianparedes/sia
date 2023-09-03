import unittest
from src.selection.RankedSelection import RankedSelection
from src.classes.Gene import Gene
from src.classes.Personajes.Arquero import Arquero
from src.classes.Personajes.Defensor import Defensor
from src.classes.Personajes.Guerrero import Guerrero
from src.classes.Personajes.Infiltrado import Infiltrado
from src.classes.Player import Player
from unittest.mock import patch
from typing import List
from unittest.mock import patch

class TestRankedSelection(unittest.TestCase):

    def setUp(self):
        gene = Gene(20, 25, 30, 15, 35, 25)

        self.individual1 = Arquero(gene)
        self.individual2 = Arquero(gene)
        self.individual3 = Guerrero(gene)
        self.individual4 = Guerrero(gene)

        self.population  = [self.individual1, self.individual2, self.individual3, self.individual4]

    @patch('random.choices')
    def test_deterministic_values(self, mock_choices):
        mock_choices.side_effect = [[self.individual2], [self.individual3], [self.individual4]]
        population: List[Player] = RankedSelection.select(self.population, 3)
        expected_population = [self.individual2, self.individual3, self.individual4]

        for i, indiviual in enumerate(population):
            self.assertEqual(indiviual, expected_population[i])
