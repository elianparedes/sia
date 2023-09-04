import unittest

from src.classes.Genotype import Genotype
from src.crossover.Annular import Annular
from unittest.mock import patch


class TestAnnular(unittest.TestCase):

    def setUp(self):
        self.gene1 = Genotype(10, 70, 20, 30, 20, 1.3)
        self.gene2 = Genotype(30, 20, 45, 40, 15, 2.0)

    @patch('random.randrange')
    def test_deterministic_values(self, mock_randrange):
        mock_randrange.side_effect = [5, 2]
        children = Annular.cross(self.gene1, self.gene2)
        self.assertEqual(children[0], Genotype.from_array([30, 70, 20, 30, 20, 2.0]))
        self.assertEqual(children[1], Genotype.from_array([10, 20, 45, 40, 15, 1.3]))

    @patch('random.randrange')
    def test_deterministic_values_two(self, mock_randrange):
        mock_randrange.side_effect = [4, 2]
        children = Annular.cross(self.gene1, self.gene2)
        self.assertEqual(children[0], Genotype.from_array([10, 70, 20, 30, 15, 2.0]))
        self.assertEqual(children[1], Genotype.from_array([30, 20, 45, 40, 20, 1.3]))

    def test_child_not_equals(self):
        #FIXME : mock probabilities
        children = Annular.cross(self.gene1, self.gene2)
        self.assertNotEqual(children[0], self.gene1)
        self.assertNotEqual(children[0], self.gene2)
        self.assertNotEqual(children[1], self.gene1)
        self.assertNotEqual(children[1], self.gene2)
        self.assertNotEqual(children[0], children[1])

    def test_same_parents(self):
        children = Annular.cross(self.gene1, self.gene1)
        self.assertEqual(children[0], self.gene1)
        self.assertEqual(children[1], self.gene1)
