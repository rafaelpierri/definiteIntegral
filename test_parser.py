import unittest

from lexer import LexerException
from parser import parse, Variable, ParserException


class TestParser(unittest.TestCase):

    def test_constant(self):
        self.assertSequenceEqual([0], parse('0'))
        self.assertSequenceEqual([123.45], parse('123.45'))

    def test_variable(self):
        self.assertSequenceEqual([Variable('x')], parse('x'))
        self.assertSequenceEqual([Variable('PI')], parse('PI'))

    def test_addsub(self):
        self.assertSequenceEqual([1, 2, 'add'], parse('1+2'))
        self.assertSequenceEqual([1, 2, 'sub'], parse('1-2'))
        self.assertSequenceEqual([1, 2, 'add', 3, 'sub'], parse('1+2-3'))

    def test_muldiv(self):
        self.assertSequenceEqual([1, 2, 'mul'], parse('1*2'))
        self.assertSequenceEqual([1, 2, 'div'], parse('1/2'))
        self.assertSequenceEqual([1, 2, 'mul', 3, 'div'], parse('1*2/3'))
        self.assertSequenceEqual([1, 2, 'div', 3, 'mul'], parse('1/2*3'))
        self.assertSequenceEqual([1, 2, 'mul', 3, 'add'], parse('1*2+3'))
        self.assertSequenceEqual([1, 2, 3, 'mul', 'add'], parse('1+2*3'))

    def test_power(self):
        self.assertSequenceEqual([1, 2, 'pow'], parse('1^2'))
        self.assertSequenceEqual([1, 2, 3, 'pow', 'pow'], parse('1^2^3'))
        self.assertSequenceEqual([1, 2, 'pow', 3, 'mul', 4, 'add'], parse('1^2*3+4'))
        self.assertSequenceEqual([1, 2, 'pow', 3, 4, 'mul', 'add'], parse('1^2+3*4'))
        self.assertSequenceEqual([1, 2, 3, 'pow', 4, 'mul', 'add'], parse('1+2^3*4'))
        self.assertSequenceEqual([1, 2, 3, 'pow', 'mul', 4, 'add'], parse('1*2^3+4'))
        self.assertSequenceEqual([1, 2, 3, 4, 'pow', 'mul', 'add'], parse('1+2*3^4'))
        self.assertSequenceEqual([1, 2, 'mul', 3, 4, 'pow', 'add'], parse('1*2+3^4'))

    def test_unary(self):
        self.assertSequenceEqual([1, 'neg'], parse('-1'))
        self.assertSequenceEqual([1], parse('+1'))
        self.assertSequenceEqual([1, 'neg', 2, 'neg', 3, 'neg', 4, 'neg', 
                'pow', 'mul', 'add'], parse('-1+-2*-3^-4'))
        self.assertSequenceEqual([1, 2, 3, 4, 'pow', 'mul', 'add'], parse('+1++2*+3^+4'))

    def test_parexp(self):
        self.assertSequenceEqual([1], parse('(1)'))
        self.assertSequenceEqual([1], parse('((1))'))
        self.assertSequenceEqual([1, 'neg', 'neg'], parse('-(-1)'))
        self.assertSequenceEqual([1, 2, 'pow', 3, 'pow'], parse('(1^2)^3'))
        self.assertSequenceEqual([1, 2, 3, 'mul', 'mul'], parse('1*(2*3)'))
        self.assertSequenceEqual([1, 2, 3, 'add', 'add'], parse('1+(2+3)'))
        self.assertSequenceEqual([1, 2, 'add', 3, 'mul', 4, 'pow', 'neg'], parse('-(((1+2)*3)^4)'))

    def test_errors_basic(self):
        with self.assertRaises(ParserException):
            parse('')

        with self.assertRaises(ParserException):
            parse('2x')

        with self.assertRaises(ParserException):
            parse('1 2')

        with self.assertRaises(ParserException):
            parse('x y')

    def test_errors_arithmetic(self):
        with self.assertRaises(ParserException):
            parse('2+')

        with self.assertRaises(ParserException):
            parse('2-')

        with self.assertRaises(ParserException):
            parse('2*')

        with self.assertRaises(ParserException):
            parse('2/')

        with self.assertRaises(ParserException):
            parse('2^')

    def test_errors_parenthesis(self):
        with self.assertRaises(ParserException):
            parse('(1+2')

        with self.assertRaises(ParserException):
            parse('1+2)')


if __name__ == '__main__':
    unittest.main()

