from argparse import ArgumentParser

from definiteIntegral import mp_defined_integral
from parser import parse


class SingleVariableFunction(object):

    def __init__(self, expr):
        self.function = parse(expr)
        names = self.function.names()
        if len(names) > 1:
            raise Exception('Too many variables.')

        self.var = names[0] if len(names) > 0 else 'x'

    def __call__(self, x):
        return self.function({self.var: x})


if __name__ == '__main__':
    argparser = ArgumentParser(description=
            'Estimates the definite integral of a single-variable function.')
    argparser.add_argument('-a', '--lower', default=0.0, type=float,
            help='Lower integration bound (default: 0.0).')
    argparser.add_argument('-b', '--upper', default=1.0, type=float,
            help='Upper integration bound (defualt: 1.0).')
    argparser.add_argument('-p', '--precision', default=1e-4, type=float,
            help='Estimation precision (default: 1e-4).')
    argparser.add_argument('-f', '--fork', default=1, type=int, 
            help='Number of worker processes.')
    argparser.add_argument('expression', help='Single-variable expression.')
    args = argparser.parse_args()

    try:
        print mp_defined_integral(SingleVariableFunction(args.expression), 
                args.lower, args.upper, args.precision, args.fork)
    except Exception, e:
        print 'ERROR: ' + str(e)

