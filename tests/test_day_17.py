import io
import unittest
from unittest import mock

from src.day_17 import findMaximumHeight, countPossibleVelocities

EXAMPLE_INPUT = "target area: x=20..30, y=-10..-5"


class TestDay17(unittest.TestCase):

    def test_single_points(self):
        # self.assertEqual(math.inf, findMaximumHeight("target area: x=0..0, y=0..0"))
        self.assertEqual(0, findMaximumHeight("target area: x=0..0, y=-1..-1"))
        self.assertEqual(1, findMaximumHeight("target area: x=0..0, y=-2..-2"))
        self.assertEqual(3, findMaximumHeight("target area: x=0..0, y=-3..-3"))
        self.assertEqual(6, findMaximumHeight("target area: x=0..0, y=-4..-4"))

    def test_first_example(self):
        self.assertEqual(45, findMaximumHeight(EXAMPLE_INPUT))

    def test_second_example(self):
        self.assertEqual(112, countPossibleVelocities(EXAMPLE_INPUT))
