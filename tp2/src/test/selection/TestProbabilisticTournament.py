import unittest
import random
from abc import ABC
from unittest.mock import patch

from src.classes.Genotype import Genotype
from src.selection.ProbabilisticTournament import ProbabilisticTournament
from src.classes.characters.Archer import Archer
from src.classes.characters.Defender import Defender
from src.classes.characters.Warrior import Warrior
from src.classes.characters.Spy import Spy

half_to_one_values = iter([0.75, 0.65, 0.85])
zero_to_one_values = iter([0.85, 0.2, 0.90])


def mock_uniform(a, b):
    if a == 0.5 and b == 1:
        return next(half_to_one_values)
    elif a == 0 and b == 1:
        return next(zero_to_one_values)
    return random.uniform(a, b)


class ProbabilisticTournamentBase(unittest.TestCase, ABC):
    INDIVIDUALS = 3
    character_class = None

    def setUp(self) -> None:
        self.population = []
        for i in range(10):
            if i != 0:
                gene = Genotype(10.0 * i, 10.0 * i, 10.0 * i, 10.0 * i, 10.0 * i, 10.0 * i)
                self.population.append(self.character_class(gene))

        self.samples = [[self.population[0], self.population[1]],
                        [self.population[1], self.population[2]],
                        [self.population[2], self.population[3]]]
        self.samples_iterator = iter(self.samples)

    def mock_sample(self):
        return next(self.samples_iterator)

    def test_results(self):
        with patch('random.uniform', side_effect=mock_uniform), \
                patch('random.sample', side_effect=lambda population, k: next(self.samples_iterator)):
            results = ProbabilisticTournament.select(self.population, self.INDIVIDUALS)

            for_test = min(self.population[0], self.population[1])
            self.assertEqual(results[0], for_test)

            for_test = max(self.population[1], self.population[2])
            self.assertEqual(results[1], for_test)

            for_test = min(self.population[2], self.population[3])
            self.assertEqual(results[2], for_test)


class TestArcher(ProbabilisticTournamentBase):
    character_class = Archer


class TestDefender(ProbabilisticTournamentBase):
    character_class = Defender


class TestWarrior(ProbabilisticTournamentBase):
    character_class = Warrior


class TestSpy(ProbabilisticTournamentBase):
    character_class = Spy
