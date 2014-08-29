class Constant(object):

    def __init__(self, value):
        self.value = value

    def __call__(self, context):
        return self.value

    def __repr__(self):
        return repr(self.value)

    def __eq__(self, other):
        try:
            return self.value == self.value
        except AttributeError:
            return False

    def names(self):
        return tuple()


class Variable(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, context):
        return float(context[self.name])

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            return False

    def names(self):
        return self.name,


class BinaryOperator(object):

    def __init__(self, symbol, left, right):
        self.left = left
        self.right = right
        self.symbol = symbol

    def __repr__(self):
        return '({} {} {})'.format(self.left, self.symbol, self.right)

    def __eq__(self, other):
        try:
            return (self.symbol == other.symbol and self.left == other.left 
                    and self.right == other.right)
        except AttributeError:
            return False

    def names(self):
        return self.left.names() + self.right.names()


class UnaryOperator(object):

    def __init__(self, operand, pre='', post=''):
        self.operand = operand
        self.pre = pre
        self.post = post

    def __repr__(self):
        return '({}{}{})'.format(self.pre, self.operand, self.post)

    def __eq__(self, other):
        try:
            return (self.pre == other.pre and self.post == other.post
                    and self.operand == other.operand)
        except AttributeError:
            return False

    def names(self):
        return self.operand.names()


class OpAdd(BinaryOperator):

    def __init__(self, left, right):
        BinaryOperator.__init__(self, '+', left, right)

    def __call__(self, context):
        return self.left(context) + self.right(context)

class OpSub(BinaryOperator):

    def __init__(self, left, right):
        BinaryOperator.__init__(self, '-', left, right)

    def __call__(self, context):
        return self.left(context) - self.right(context)

class OpMul(BinaryOperator):

    def __init__(self, left, right):
        BinaryOperator.__init__(self, '*', left, right)

    def __call__(self, context):
        return self.left(context) * self.right(context)

class OpDiv(BinaryOperator):

    def __init__(self, left, right):
        BinaryOperator.__init__(self, '/', left, right)

    def __call__(self, context):
        return self.left(context) / self.right(context)

class OpPow(BinaryOperator):

    def __init__(self, left, right):
        BinaryOperator.__init__(self, '^', left, right)

    def __call__(self, context):
        return self.left(context) ** self.right(context)

class OpNeg(UnaryOperator):

    def __init__(self, value):
        UnaryOperator.__init__(self, value, pre='-')

    def __call__(self, context):
        return -self.operand(context)


OPERATIONS = {
    'add': (2, OpAdd),
    'sub': (2, OpSub),
    'mul': (2, OpMul),
    'div': (2, OpDiv),
    'pow': (2, OpPow),
    'neg': (1, OpNeg),
}


def build(expr):
    s = []
    for e in expr:
        try:
            op = OPERATIONS[e]
            if op[0] == 1:
                v = s.pop()
                s.append(op[1](v))
            elif op[0] == 2:
                r = s.pop()
                l = s.pop()
                s.append(op[1](l, r))
        except KeyError:
            if callable(e):
                # Variable
                s.append(e)
            else:
                s.append(Constant(e))
    return s.pop()

