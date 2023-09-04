import unittest
from abc import ABC
from unittest.mock import patch

from src.classes.Genotype import Genotype
from src.selection.DeterministicTournament import DeterministicTournament
from src.classes.characters.Archer import Archer
from src.classes.characters.Defender import Defender
from src.classes.characters.Warrior import Warrior
from src.classes.characters.Spy import Spy


class DeterministicTournamentBase(unittest.TestCase, ABC):
    INDIVIDUALS = 3
    character_class = None

    def setUp(self) -> None:
        self.population = []
        DeterministicTournament.tournament_size = None
        for i in range(10):
            if i != 0:
                gene = Genotype(10.0 * i, 10.0 * i, 10.0 * i, 10.0 * i, 10.0 * i, 10.0 * i)
                self.population.append(self.character_class(gene))

    def test_size_not_set(self):
        with self.assertRaises(ValueError):
            DeterministicTournament.select(self.population, self.INDIVIDUALS)

    @patch('random.sample')
    def test_results(self, mock_sample):
        DeterministicTournament.set_tournament_size(2)
        mock_sample.side_effect = [[self.population[0], self.population[1]],
                                   [self.population[1], self.population[2]],
                                   [self.population[2], self.population[3]]]
        result = DeterministicTournament.select(self.population, self.INDIVIDUALS)
        sorted(result)
        for i, player in enumerate(result):
            self.assertEqual(player, max(self.population[i], self.population[i + 1]))


class TestArcher(DeterministicTournamentBase):
    character_class = Archer


class TestDefender(DeterministicTournamentBase):
    character_class = Defender


class TestWarrior(DeterministicTournamentBase):
    character_class = Warrior


class TestSpy(DeterministicTournamentBase):
    character_class = Spy
