import unittest
from abc import ABC
from unittest.mock import patch

from src.classes.Genotype import Genotype
from src.selection.DeterministicTournament import DeterministicTournament
from src.classes.characters.Archer import Arquero
from src.classes.characters.Defender import Defensor
from src.classes.characters.Warrior import Guerrero
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


class TestArquero(DeterministicTournamentBase):
    character_class = Arquero


class TestDefensor(DeterministicTournamentBase):
    character_class = Defensor


class TestGuerrero(DeterministicTournamentBase):
    character_class = Guerrero


class TestInfiltrado(DeterministicTournamentBase):
    character_class = Spy
