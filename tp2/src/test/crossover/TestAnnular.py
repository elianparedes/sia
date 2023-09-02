import unittest
from src.crossover.Annular import Annular
from src.classes.Gene import Gene
from unittest.mock import patch


class TestAnnular(unittest.TestCase):

    def setUp(self):
        self.gene1 = Gene(1, 2, 3, 4, 5, 6)
        self.gene2 = Gene(10, 20, 30, 40, 50, 60)

    @patch('random.randrange')
    def test_deterministic_values(self, mock_randrange):
        mock_randrange.side_effect = [5, 2]
        children = Annular.cross(self.gene1, self.gene2)
        self.assertEqual(children[0], Gene.from_array([10, 2, 3, 4, 5, 60]))
        self.assertEqual(children[1], Gene.from_array([1, 20, 30, 40, 50, 6]))

    @patch('random.randrange')
    def test_deterministic_values_two(self, mock_randrange):
        mock_randrange.side_effect = [4, 2]
        children = Annular.cross(self.gene1, self.gene2)
        self.assertEqual(children[0], Gene.from_array([1, 2, 3, 4, 50, 60]))
        self.assertEqual(children[1], Gene.from_array([10, 20, 30, 40, 5, 6]))

    def test_child_not_equals(self):
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