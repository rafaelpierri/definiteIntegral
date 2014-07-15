from lexer import Lexer

class ParserException(Exception):

    def __init__(self, msg, token=(None,)):
        Exception.__init__(self, msg)
        self.token = token

    def __str__(self):
        if self.token[0] is None:
            return self.message + ' (at end of input)'
        else:
            return '{} ("{}" at position {})'.format(self.message, 
                    self.token[1], self.token[2])


class Variable(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __call__(self, context):
        return context[self.name]

    def __eq__(self, other):
        return self.name == other.name


class Parser(object):

    def parse(self, src):
        self.expr = []
        with Lexer(src) as lexer:
            try:
                self.lexer = lexer
                t = lexer.next()
                if t[0] not in ('+', '-', '(', 'number', 'name'):
                    raise ParserException('Unexpected token', t)

                t = self.addsub(t)
                if t[0] is not None:
                    raise ParserException('Unexpected token', t)
            except StopIteration:
                raise ParserException('Unexpected end of input')
            finally:
                self.lexer = None

        return self.expr

    def addsub(self, t):
        if t[0] not in ('+', '-', '(', 'number', 'name'):
            raise ParserException('Unexpected token', t)

        t = self.muldiv(t)
        while t[0] == '+' or t[0] == '-':
            op = 'add' if t[0] == '+' else 'sub'
            t = self.muldiv(self.lexer.next())
            self.expr.append(op)
        return t

    def muldiv(self, t):
        if t[0] not in ('+', '-', '(', 'number', 'name'):
            raise ParserException('Unexpected token', t)

        t = self.power(t)
        while t[0] == '*' or t[0] == '/':
            op = 'mul' if t[0] == '*' else 'div'
            t = self.power(self.lexer.next())
            self.expr.append(op)
        return t

    def power(self, t):
        if t[0] not in ('+', '-', '(', 'number', 'name'):
            raise ParserException('Unexpected token', t)

        substack = 0
        t = self.unary(t)
        while t[0] == '^':
            substack += 1
            t = self.unary(self.lexer.next())
        else:
            self.expr.extend(['pow'] * substack)
        return t

    def unary(self, t):
        if t[0] not in ('+', '-', '(', 'number', 'name'):
            raise ParserException('Unexpected token', t)

        if t[0] == '-':
            t = self.parexp(self.lexer.next())
            self.expr.append('neg')
            return t
        elif t[0] == '+':
            return self.parexp(self.lexer.next())
        else:
            return self.parexp(t)

    def parexp(self, t):
        if t[0] not in ('(', 'number', 'name'):
            raise ParserException('Unexpected token', t)

        if t[0] == 'number':
            value = float(t[1])
            if value.is_integer():
                value = int(value)
            self.expr.append(value)
            return self.lexer.next()
        elif t[0] == 'name':
            self.expr.append(Variable(t[1]))
            return self.lexer.next()
        
        # t is left parenthesis
        t = self.addsub(self.lexer.next())
        if t[0] != ')':
            raise ParserException('Unexpected token', t)
        return self.lexer.next()


def parse(src):
    return Parser().parse(src)

