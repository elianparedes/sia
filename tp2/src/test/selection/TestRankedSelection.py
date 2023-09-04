import unittest
from typing import List
from unittest.mock import patch

from src.classes.Genotype import Genotype
from src.classes.characters.CharacterABC import CharacterABC
from src.classes.characters.Archer import Archer
from src.classes.characters.Warrior import Warrior
from src.selection.Ranked import Ranked


class TestRankedSelection(unittest.TestCase):

    def setUp(self):
        gene = Genotype(20, 25, 30, 15, 35, 25)

        self.individual1 = Archer(gene)
        self.individual2 = Archer(gene)
        self.individual3 = Warrior(gene)
        self.individual4 = Warrior(gene)

        self.population = [self.individual1, self.individual2, self.individual3, self.individual4]

    @patch('random.choices')
    def test_deterministic_values(self, mock_choices):
        mock_choices.side_effect = [[self.individual2], [self.individual3], [self.individual4]]
        population: List[CharacterABC] = Ranked.select(self.population, 3)
        expected_population = [self.individual2, self.individual3, self.individual4]

        for i, individual in enumerate(population):
            self.assertEqual(individual, expected_population[i])
