class LexerException(Exception):

    def __init__(self, pos, msg):
        Exception.__init__(self, msg)
        self.pos = pos

    def __str__(self):
        return '{} @{}'.format(self.message, self.pos)


def tokens(src):
    i = iter(zip(src, range(len(src))))
    c, p = next(i)
    while True:
        p0 = p
        if c is None:
            # end of input
            raise StopIteration
        elif c in (' ', '\t'):
            # discard whitespace
            c, p = next(i)
        elif '0' <= c <= '9':
            t, c, p = number_token(i, c, p)
            yield ('number', t, p0)
        elif 'a' <= c.lower() <= 'z':
            t, c, p = bareword_token(i, c, p)
            # there are no keywords, so
            # everything (else) is an identifier
            yield ('name', t, p0)
        else:
            t, c, p = symbol_token(i, c, p)
            yield (t, t, p0)

def number_token(i, c, pos):
    # /^\d+(\.\d+)?/
    try:
        token = ''
        while '0' <= c <= '9':
            token += c
            c, p = next(i)

        if c == '.':
            try:
                token += '.'
                c, p = next(i)
            except StopIteration:
                raise LexerException(pos, 'Invalid number')
                
            if not '0' <= c <= '9':
                raise LexerException(pos, 'Invalid number')

            while '0' <= c <= '9':
                token += c
                c, p = next(i)

        return (token, c, p)
    except StopIteration:
        return (token, None, None)

def bareword_token(i, c, p):
    # /^[a-zA-Z][a-zA-Z0-9_]*/
    try:
        token = c
        c, p = next(i)
        while 'a' <= c.lower() <= 'z' or '0' <= c <= '9' or c == '_':
            token += c
            c, p = next(i)
        return (token, c, p)
    except StopIteration:
        return (token, None, None)

def symbol_token(i, c, p):
    # /[+-*\/^]/
    try:
        if c not in '+-*/^()':
            raise LexerException(p, 'Invalid symbol')

        token = c
        c, p = next(i)
        return (token, c, p)
    except StopIteration:
        return (token, None, None)


