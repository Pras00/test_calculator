import unittest
from unittest.mock import patch
from calculator import calculator

class TestCalculator(unittest.TestCase):

    # Penjumlahan
    @patch('builtins.input', side_effect=["1", "2", "3"])
    def test_jumlah_calculator(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 5)

    # Pengurangan
    @patch('builtins.input', side_effect=["2", "9", "5"])
    def test_kurang_calculator(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 4)

    # Perkalian
    @patch('builtins.input', side_effect=["3", "4", "3"])
    def test_kali_calculator(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 12)

    # Pembagian
    @patch('builtins.input', side_effect=["4", "10", "2"])
    def test_bagi_calculator(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()