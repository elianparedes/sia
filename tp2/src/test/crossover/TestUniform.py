import unittest

from src.classes.Genotype import Genotype
from src.crossover.Uniform import Uniform
from unittest.mock import patch


class TestUniform(unittest.TestCase):

    def setUp(self):
        self.gene1 = Genotype(20, 40, 60, 10, 20, 1.5)
        self.gene2 = Genotype(30, 40, 60, 5, 15, 1.7)

    @patch('random.random')
    def test_deterministic_values(self, mock_random):
        mock_random.side_effect = [0.1, 0.1, 0.7, 0.7, 0.1, 0.7]
        children = Uniform.cross(self.gene1, self.gene2)
        self.assertEqual(children[0], Genotype.from_array([30, 40, 60, 10, 15, 1.5]))
        self.assertEqual(children[1], Genotype.from_array([20, 40, 60, 5, 20, 1.7]))

    def test_child_not_equals(self):
        children = Uniform.cross(self.gene1, self.gene2)
        self.assertNotEqual(children[0], self.gene1)
        self.assertNotEqual(children[0], self.gene2)
        self.assertNotEqual(children[1], self.gene1)
        self.assertNotEqual(children[1], self.gene2)
        self.assertNotEqual(children[0], children[1])

    def test_same_parents(self):
        children = Uniform.cross(self.gene1, self.gene1)
        self.assertEqual(children[0], self.gene1)
        self.assertEqual(children[1], self.gene1)
