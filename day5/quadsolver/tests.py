import sys
import unittest

from day5.quadsolver import main, cli


class TestQuadratricSolver(unittest.TestCase):
    def test_simple(self):
        """Sanity test"""
        x1, x2 = main.solve_quadratic(1, 2, 1)
        # assertions
        self.assertIsInstance(x1, complex)
        self.assertIsInstance(x2, complex)
        # validate values
        self.assertEqual((complex(-1, 0), complex(-1, 0)), (x1, x1))

    def test_negative(self):
        """Test for correct types"""
        with self.assertRaises(ValueError):
            _ = main.solve_quadratic('a', 'b', 'c')


class TestCLI(unittest.TestCase):
    def test_coefficients(self):
        """Coefficients handling"""
        sys.argv = "python 1 2 1".split(' ')
        args = cli.parse_args()
        self.assertEqual((1.0, 2.0, 1.0), args.coefficients)
