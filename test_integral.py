import unittest

from definiteIntegral import defined_integral, mp_defined_integral

def ident(x):
    return x

class TestIntegral(unittest.TestCase):

    def test_precision(self):
        self.assertAlmostEqual(0.5, defined_integral(ident, 0, 1, 1), delta=1)
        self.assertAlmostEqual(0.5, defined_integral(ident, 0, 1, 0.01), delta=0.01)
        self.assertAlmostEqual(0.5, defined_integral(ident, 0, 1, 0.0001), delta=0.0001)
        self.assertAlmostEqual(0.5, defined_integral(ident, 0, 1, 0.000001), delta=0.000001)

    def test_lower(self):
        self.assertAlmostEqual(-1.5, defined_integral(ident, -2, 1), delta=0.0001)
        self.assertAlmostEqual(0.0, defined_integral(ident, -1, 1), delta=0.0001)
        self.assertAlmostEqual(0.5, defined_integral(ident, 0, 1), delta=0.0001)
        self.assertAlmostEqual(0.095, defined_integral(ident, 0.9, 1), delta=0.0001)

    def test_upper(self):
        self.assertAlmostEqual(0.005, defined_integral(ident, 0, 0.1), delta=0.0001)
        self.assertAlmostEqual(0.5, defined_integral(ident, 0, 1), delta=0.0001)
        self.assertAlmostEqual(2.0, defined_integral(ident, 0, 2), delta=0.0001)
        self.assertAlmostEqual(50.0, defined_integral(ident, 0, 10), delta=0.0001)

    def test_exponent(self):
        self.assertAlmostEqual(0.5000, defined_integral(lambda x: x ** -2, 1, 2), delta=0.0001)
        self.assertAlmostEqual(0.6931, defined_integral(lambda x: x ** -1, 1, 2), delta=0.0001)
        self.assertAlmostEqual(0.8284, defined_integral(lambda x: x ** -0.5, 1, 2), delta=0.0001)
        self.assertAlmostEqual(1.0000, defined_integral(lambda x: x ** 0, 1, 2), delta=0.0001)
        self.assertAlmostEqual(1.2190, defined_integral(lambda x: x ** 0.5, 1, 2), delta=0.0001)
        self.assertAlmostEqual(1.5000, defined_integral(lambda x: x ** 1, 1, 2), delta=0.0001)
        self.assertAlmostEqual(2.3333, defined_integral(lambda x: x ** 2, 1, 2), delta=0.0001)

    def test_mp(self):
        self.assertAlmostEqual(0.5, mp_defined_integral(ident, 0, 1, 0.001, 1), delta=0.001)
        self.assertAlmostEqual(0.5, mp_defined_integral(ident, 0, 1, 0.000001, 4), delta=0.000001)
        self.assertAlmostEqual(0.5, mp_defined_integral(ident, 0, 1, 0.000001, 16), delta=0.000001)

if __name__ == '__main__':
    unittest.main()

