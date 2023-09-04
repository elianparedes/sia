import unittest
from typing import List
from unittest.mock import patch

from src.classes.Genotype import Genotype
from src.classes.Player import Player
from src.classes.characters.Arquero import Arquero
from src.classes.characters.Guerrero import Guerrero
from src.selection.Ranked import Ranked


class TestRankedSelection(unittest.TestCase):

    def setUp(self):
        gene = Genotype(20, 25, 30, 15, 35, 25)

        self.individual1 = Arquero(gene)
        self.individual2 = Arquero(gene)
        self.individual3 = Guerrero(gene)
        self.individual4 = Guerrero(gene)

        self.population = [self.individual1, self.individual2, self.individual3, self.individual4]

    @patch('random.choices')
    def test_deterministic_values(self, mock_choices):
        mock_choices.side_effect = [[self.individual2], [self.individual3], [self.individual4]]
        population: List[Player] = Ranked.select(self.population, 3)
        expected_population = [self.individual2, self.individual3, self.individual4]

        for i, indiviual in enumerate(population):
            self.assertEqual(indiviual, expected_population[i])
