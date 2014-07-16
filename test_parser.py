import unittest

from function import Variable
from parser import Parser, ParserException


class TestParser(unittest.TestCase):

    def parse(self, src):
        return Parser().parse(src)

    def test_constant(self):
        self.assertSequenceEqual([0], self.parse('0'))
        self.assertSequenceEqual([123.45], self.parse('123.45'))

    def test_variable(self):
        self.assertSequenceEqual([Variable('x')], self.parse('x'))
        self.assertSequenceEqual([Variable('PI')], self.parse('PI'))

    def test_addsub(self):
        self.assertSequenceEqual([1, 2, 'add'], self.parse('1+2'))
        self.assertSequenceEqual([1, 2, 'sub'], self.parse('1-2'))
        self.assertSequenceEqual([1, 2, 'add', 3, 'sub'], self.parse('1+2-3'))

    def test_muldiv(self):
        self.assertSequenceEqual([1, 2, 'mul'], self.parse('1*2'))
        self.assertSequenceEqual([1, 2, 'div'], self.parse('1/2'))
        self.assertSequenceEqual([1, 2, 'mul', 3, 'div'], self.parse('1*2/3'))
        self.assertSequenceEqual([1, 2, 'div', 3, 'mul'], self.parse('1/2*3'))
        self.assertSequenceEqual([1, 2, 'mul', 3, 'add'], self.parse('1*2+3'))
        self.assertSequenceEqual([1, 2, 3, 'mul', 'add'], self.parse('1+2*3'))

    def test_power(self):
        self.assertSequenceEqual([1, 2, 'pow'], self.parse('1^2'))
        self.assertSequenceEqual([1, 2, 3, 'pow', 'pow'], self.parse('1^2^3'))
        self.assertSequenceEqual([1, 2, 'pow', 3, 'mul', 4, 'add'], self.parse('1^2*3+4'))
        self.assertSequenceEqual([1, 2, 'pow', 3, 4, 'mul', 'add'], self.parse('1^2+3*4'))
        self.assertSequenceEqual([1, 2, 3, 'pow', 4, 'mul', 'add'], self.parse('1+2^3*4'))
        self.assertSequenceEqual([1, 2, 3, 'pow', 'mul', 4, 'add'], self.parse('1*2^3+4'))
        self.assertSequenceEqual([1, 2, 3, 4, 'pow', 'mul', 'add'], self.parse('1+2*3^4'))
        self.assertSequenceEqual([1, 2, 'mul', 3, 4, 'pow', 'add'], self.parse('1*2+3^4'))

    def test_unary(self):
        self.assertSequenceEqual([1, 'neg'], self.parse('-1'))
        self.assertSequenceEqual([1], self.parse('+1'))
        self.assertSequenceEqual([1, 'neg', 2, 'neg', 3, 'neg', 4, 'neg', 
                'pow', 'mul', 'add'], self.parse('-1+-2*-3^-4'))
        self.assertSequenceEqual([1, 2, 3, 4, 'pow', 'mul', 'add'], self.parse('+1++2*+3^+4'))

    def test_parexp(self):
        self.assertSequenceEqual([1], self.parse('(1)'))
        self.assertSequenceEqual([1], self.parse('((1))'))
        self.assertSequenceEqual([1, 'neg', 'neg'], self.parse('-(-1)'))
        self.assertSequenceEqual([1, 2, 'pow', 3, 'pow'], self.parse('(1^2)^3'))
        self.assertSequenceEqual([1, 2, 3, 'mul', 'mul'], self.parse('1*(2*3)'))
        self.assertSequenceEqual([1, 2, 3, 'add', 'add'], self.parse('1+(2+3)'))
        self.assertSequenceEqual([1, 2, 'add', 3, 'mul', 4, 'pow', 'neg'], self.parse('-(((1+2)*3)^4)'))

    def test_errors_basic(self):
        with self.assertRaises(ParserException):
            self.parse('')

        with self.assertRaises(ParserException):
            self.parse('2x')

        with self.assertRaises(ParserException):
            self.parse('1 2')

        with self.assertRaises(ParserException):
            self.parse('x y')

    def test_errors_arithmetic(self):
        with self.assertRaises(ParserException):
            self.parse('2+')

        with self.assertRaises(ParserException):
            self.parse('2-')

        with self.assertRaises(ParserException):
            self.parse('2*')

        with self.assertRaises(ParserException):
            self.parse('2/')

        with self.assertRaises(ParserException):
            self.parse('2^')

    def test_errors_parenthesis(self):
        with self.assertRaises(ParserException):
            self.parse('(1+2')

        with self.assertRaises(ParserException):
            self.parse('1+2)')


if __name__ == '__main__':
    unittest.main()

