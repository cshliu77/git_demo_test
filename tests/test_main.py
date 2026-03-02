import unittest
from unittest.mock import patch
import subprocess
import sys
import os

# 將專案根目錄加入 path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import (
    additionMethod,
    subtractionMethod,
    divisionMethod,
    multiplicationMethod,
    hello_world_en,
    hello_world_zh,
)


class TestAdditionMethod(unittest.TestCase):
    """測試加法函式"""

    def test_positive_numbers(self):
        self.assertEqual(additionMethod(3, 5), 8)

    def test_negative_numbers(self):
        self.assertEqual(additionMethod(-3, -5), -8)

    def test_mixed_sign(self):
        self.assertEqual(additionMethod(-3, 5), 2)

    def test_zero(self):
        self.assertEqual(additionMethod(0, 0), 0)

    def test_float(self):
        self.assertAlmostEqual(additionMethod(1.5, 2.3), 3.8)


class TestSubtractionMethod(unittest.TestCase):
    """測試減法函式"""

    def test_positive_numbers(self):
        self.assertEqual(subtractionMethod(10, 3), 7)

    def test_negative_result(self):
        self.assertEqual(subtractionMethod(3, 10), -7)

    def test_negative_numbers(self):
        self.assertEqual(subtractionMethod(-3, -5), 2)

    def test_zero(self):
        self.assertEqual(subtractionMethod(0, 0), 0)

    def test_float(self):
        self.assertAlmostEqual(subtractionMethod(5.5, 2.2), 3.3)


class TestDivisionMethod(unittest.TestCase):
    """測試除法函式"""

    def test_exact_division(self):
        self.assertEqual(divisionMethod(10, 2), 5.0)

    def test_non_exact_division(self):
        self.assertAlmostEqual(divisionMethod(10, 3), 3.3333333333)

    def test_negative_numbers(self):
        self.assertEqual(divisionMethod(-10, 2), -5.0)

    def test_divide_zero_by_number(self):
        self.assertEqual(divisionMethod(0, 5), 0.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divisionMethod(10, 0)


class TestMultiplicationMethod(unittest.TestCase):
    """測試乘法函式"""

    def test_positive_numbers(self):
        self.assertEqual(multiplicationMethod(3, 5), 15)

    def test_negative_numbers(self):
        self.assertEqual(multiplicationMethod(-3, -5), 15)

    def test_mixed_sign(self):
        self.assertEqual(multiplicationMethod(-3, 5), -15)

    def test_zero(self):
        self.assertEqual(multiplicationMethod(0, 100), 0)

    def test_float(self):
        self.assertAlmostEqual(multiplicationMethod(2.5, 4.0), 10.0)


class TestHelloWorld(unittest.TestCase):
    """測試問候函式"""

    @patch("builtins.print")
    def test_hello_world_en(self, mock_print):
        hello_world_en()
        mock_print.assert_called_once_with("Hello, World!")

    @patch("builtins.print")
    def test_hello_world_zh(self, mock_print):
        hello_world_zh()
        mock_print.assert_called_once_with("哈囉！世界！")


class TestCLI(unittest.TestCase):
    """測試 CLI 主程式入口"""

    def _run_main(self, *args):
        """執行 main.py 並回傳 stdout"""
        main_path = os.path.join(os.path.dirname(__file__), "..", "main.py")
        result = subprocess.run(
            [sys.executable, main_path, *args],
            capture_output=True,
            text=True,
        )
        return result

    def test_addition(self):
        result = self._run_main("10", "+", "5")
        self.assertIn("15", result.stdout)

    def test_subtraction(self):
        result = self._run_main("10", "-", "3")
        self.assertIn("7", result.stdout)

    def test_multiplication(self):
        result = self._run_main("4", "*", "5")
        self.assertIn("20", result.stdout)

    def test_division(self):
        result = self._run_main("10", "/", "2")
        self.assertIn("5.0", result.stdout)

    def test_not_enough_arguments(self):
        result = self._run_main("10", "+")
        self.assertIn("Not enough arguments", result.stdout)

    def test_unsupported_operator(self):
        result = self._run_main("10", "%", "3")
        self.assertIn("Unsupported operator", result.stdout)


if __name__ == "__main__":
    unittest.main()
