import unittest

from lexer import tokens, LexerException


class TestLexer(unittest.TestCase):

    def test_number(self):
        self.assertSequenceEqual([('number', '0', 0), (None, '', 1)], tuple(tokens('0')))
        self.assertSequenceEqual([('number', '123', 0), (None, '', 3)], tuple(tokens('123')))
        self.assertSequenceEqual([('number', '123.45', 0), (None, '', 6)], tuple(tokens('123.45')))

        with self.assertRaises(LexerException):
            tuple(tokens('123.'))

        with self.assertRaises(LexerException):
            tuple(tokens('.123'))

    def test_bareword(self):
        self.assertSequenceEqual([('name', 'some_token', 0), (None, '', 10)], tuple(tokens('some_token')))
        self.assertSequenceEqual([('name', 'SomeToken', 0), (None, '', 9)], tuple(tokens('SomeToken')))

    def test_symbol(self):
        self.assertSequenceEqual([('+', '+', 0), (None, '', 1)], tuple(tokens('+')))
        self.assertSequenceEqual([('-', '-', 0), (None, '', 1)], tuple(tokens('-')))
        self.assertSequenceEqual([('*', '*', 0), (None, '', 1)], tuple(tokens('*')))
        self.assertSequenceEqual([('/', '/', 0), (None, '', 1)], tuple(tokens('/')))
        self.assertSequenceEqual([('^', '^', 0), (None, '', 1)], tuple(tokens('^')))
        self.assertSequenceEqual([('(', '(', 0), (None, '', 1)], tuple(tokens('(')))
        self.assertSequenceEqual([(')', ')', 0), (None, '', 1)], tuple(tokens(')')))

        with self.assertRaises(LexerException):
            tuple(tokens('.'))

    def test_tokens(self):
        self.assertSequenceEqual([('number', '2', 1), ('name', 'a', 2), ('+', '+', 4),
                ('name', 'b', 6), ('^', '^', 7), ('number', '2', 8), ('*', '*', 10),
                ('name', 'sin', 13), ('(', '(', 16), ('-', '-', 17), ('name', 'PI', 18),
                ('/', '/', 20), ('number', '2.0', 21), (')', ')', 24), (None, '', 26)], 
                tuple(tokens(' 2a + b^2 *  sin(-PI/2.0) ')))

if __name__ == '__main__':
    unittest.main()

