import unittest

from parser import parse


class TestFunction(unittest.TestCase):

    def test_constant_zero(self):
        f = parse('0')
        self.assertAlmostEquals(0, f({'x': 0}))
        self.assertAlmostEquals(0, f({'x': 1}))

    def test_constant_non_zero(self):
        f = parse('1')
        self.assertAlmostEquals(1, f({'x': 0}))
        self.assertAlmostEquals(1, f({'x': 1}))

    def test_variable(self):
        f = parse('x')
        self.assertAlmostEquals(0, f({'x': 0}))
        self.assertAlmostEquals(1, f({'x': 1}))

    def test_add(self):
        f = parse('1 + 2')
        self.assertAlmostEquals(3, f({'x': 0}))
        self.assertAlmostEquals(3, f({'x': 1}))

        f = parse('x + 1')
        self.assertAlmostEquals(1, f({'x': 0}))
        self.assertAlmostEquals(2, f({'x': 1}))

        f = parse('x + y')
        self.assertAlmostEquals(5, f({'x': 2, 'y': 3}))
        self.assertAlmostEquals(9, f({'x': 4, 'y': 5}))

    def test_sub(self):
        f = parse('1 - 2')
        self.assertAlmostEquals(-1, f({'x': 0}))
        self.assertAlmostEquals(-1, f({'x': 1}))

        f = parse('x - 1')
        self.assertAlmostEquals(-1, f({'x': 0}))
        self.assertAlmostEquals(0, f({'x': 1}))

        f = parse('x - y')
        self.assertAlmostEquals(-1, f({'x': 2, 'y': 3}))
        self.assertAlmostEquals(4, f({'x': 5, 'y': 1}))

    def test_mul(self):
        f = parse('2 * 3')
        self.assertAlmostEquals(6, f({'x': 0}))
        self.assertAlmostEquals(6, f({'x': 1}))

        f = parse('x * 2')
        self.assertAlmostEquals(0, f({'x': 0}))
        self.assertAlmostEquals(2, f({'x': 1}))

        f = parse('x * y')
        self.assertAlmostEquals(8, f({'x': 2, 'y': 4}))
        self.assertAlmostEquals(15, f({'x': 3, 'y': 5}))

    def test_div(self):
        f = parse('1 / 2')
        self.assertAlmostEquals(0.5, f({'x': 0}))
        self.assertAlmostEquals(0.5, f({'x': 1}))

        f = parse('x / 2')
        self.assertAlmostEquals(1.5, f({'x': 3}))
        self.assertAlmostEquals(2.0, f({'x': 4}))

        f = parse('x / y')
        self.assertAlmostEquals(0.6666667, f({'x': 2, 'y': 3}))
        self.assertAlmostEquals(2.5000000, f({'x': 5, 'y': 2}))

    def test_pow(self):
        f = parse('2 ^ 3')
        self.assertAlmostEquals(8, f({'x': 0}))
        self.assertAlmostEquals(8, f({'x': 1}))

        f = parse('x ^ 2')
        self.assertAlmostEquals(0, f({'x': 0}))
        self.assertAlmostEquals(4, f({'x': 2}))

        f = parse('x ^ y')
        self.assertAlmostEquals(16, f({'x': 2, 'y': 4}))
        self.assertAlmostEquals(27, f({'x': 3, 'y': 3}))

    def test_neg(self):
        f = parse('-2')
        self.assertAlmostEquals(-2, f({'x': 0}))
        self.assertAlmostEquals(-2, f({'x': 1}))

        f = parse('-x')
        self.assertAlmostEquals(-3, f({'x': 3}))
        self.assertAlmostEquals(-4, f({'x': 4}))


if __name__ == '__main__':
    unittest.main()

