import io
import unittest
from unittest import mock

from src.day_16 import calcVersionSum, calcVersionSumFromFile, toBinaryString, calcExpression, calcExpressionFromFile

EXAMPLE_INPUT = """8A004A801A8002F478"""


class TestDay16(unittest.TestCase):

    def test_hex_string_conversion(self):
        self.assertEqual("00000001", toBinaryString("01"))
        self.assertEqual("00111000000000000110111101000101001010010001001000000000", toBinaryString("38006F45291200"))

    def test_single_literal(self):
        self.assertEqual(6, calcVersionSum("D2FE28"))

    def test_zero_length_type(self):
        self.assertEqual(9, calcVersionSum("38006F45291200"))

    def test_one_length_type(self):
        self.assertEqual(14, calcVersionSum("EE00D40C823060"))

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_16.open', return_value=fake_file, create=True):
            self.assertEqual(16, calcVersionSumFromFile("test.txt"))

    def test_sum(self):
        self.assertEqual(3, calcExpression("C200B40A82"))

    def test_product(self):
        self.assertEqual(54, calcExpression("04005AC33890"))

    def test_minimum(self):
        self.assertEqual(7, calcExpression("880086C3E88112"))

    def test_maximum(self):
        self.assertEqual(9, calcExpression("CE00C43D881120"))

    def test_less_than(self):
        self.assertEqual(1, calcExpression("D8005AC2A8F0"))

    def test_greater_than(self):
        self.assertEqual(0, calcExpression("F600BC2D8F"))

    def test_equality(self):
        self.assertEqual(0, calcExpression("9C005AC2F8F0"))

    def test_multi_example(self):
        fake_file = io.StringIO("9C0141080250320F1802104A08")
        with mock.patch('src.day_16.open', return_value=fake_file, create=True):
            self.assertEqual(1, calcExpressionFromFile("test.txt"))
