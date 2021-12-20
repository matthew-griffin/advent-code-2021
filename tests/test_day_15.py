import io
import unittest
from unittest import mock

from src.day_15 import calcLowestRisk, calcLowestRiskPart2, calcMultiGridCost

EXAMPLE_INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


class TestDay15(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_15.open', return_value=fake_file, create=True):
            self.assertEqual(40, calcLowestRisk("test.txt"))

    def test_reversing_example(self):
        fake_file = io.StringIO("""19999
        19111
        11191
        99991
        99991""")
        with mock.patch('src.day_15.open', return_value=fake_file, create=True):
            self.assertEqual(10, calcLowestRisk("test.txt"))

    def test_multi_grid_calculation(self):
        self.assertEqual(8, calcMultiGridCost([[8]], 1, 1, (0, 0)))
        self.assertEqual(9, calcMultiGridCost([[8]], 1, 1, (1, 0)))
        self.assertEqual(9, calcMultiGridCost([[8]], 1, 1, (0, 1)))
        self.assertEqual(1, calcMultiGridCost([[8]], 1, 1, (1, 1)))
        self.assertEqual(2, calcMultiGridCost([[8]], 1, 1, (2, 1)))
        self.assertEqual(1, calcMultiGridCost([[8]], 1, 1, (6, 5)))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_15.open', return_value=fake_file, create=True):
            self.assertEqual(315, calcLowestRiskPart2("test.txt"))
